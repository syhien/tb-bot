/* ========================================
   淘宝联盟搜索系统 - 自定义JavaScript
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
  // 初始化所有功能
  initToastNotifications();
  initSearchForm();
  initCopyButtons();
  initLoadingState();
});

/* ========================================
   Toast 通知系统
   ======================================== */

function initToastNotifications() {
  // 创建toast容器（如果不存在）
  if (!document.querySelector('.toast-container')) {
    const container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }
}

/**
 * 显示Toast通知
 * @param {string} message - 消息内容
 * @param {string} type - 类型：success, error, info
 * @param {number} duration - 显示时长（毫秒）
 */
function showToast(message, type = 'info', duration = 3000) {
  const container = document.querySelector('.toast-container');
  if (!container) return;

  // 创建toast元素
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;

  // 添加图标
  const icon = getIconForType(type);
  toast.innerHTML = `
    <span class="icon">${icon}</span>
    <span>${message}</span>
  `;

  // 添加点击关闭功能
  toast.addEventListener('click', function() {
    removeToast(toast);
  });

  // 添加到容器
  container.appendChild(toast);

  // 自动移除
  setTimeout(() => {
    removeToast(toast);
  }, duration);
}

/**
 * 移除Toast（带动画）
 */
function removeToast(toast) {
  toast.style.animation = 'toast-out 0.3s ease forwards';
  setTimeout(() => {
    if (toast.parentNode) {
      toast.parentNode.removeChild(toast);
    }
  }, 300);
}

/**
 * 根据类型获取图标
 */
function getIconForType(type) {
  const icons = {
    success: '✓',
    error: '✕',
    info: 'ℹ'
  };
  return icons[type] || icons.info;
}

/* ========================================
   搜索表单增强
   ======================================== */

function initSearchForm() {
  const searchForm = document.querySelector('form');
  const searchInput = document.querySelector('input[name="keyword"]');
  const searchButton = searchForm?.querySelector('button[type="submit"]');

  if (!searchForm || !searchInput || !searchButton) return;

  searchForm.addEventListener('submit', function(e) {
    const keyword = searchInput.value.trim();

    if (!keyword) {
      e.preventDefault();
      showToast('请输入搜索关键词', 'error');
      searchInput.focus();
      return;
    }

    e.preventDefault();
    startStreamingSearch(keyword);
  });
}

function startStreamingSearch(keyword) {
  var container = document.querySelector('.container');
  container.innerHTML =
    '<div class="card mb-4 fade-in search-compact"><div class="card-body">' +
      '<form id="streamSearchForm" method="POST" action="/search">' +
        '<div class="input-group">' +
          '<input type="text" class="form-control" id="keyword" name="keyword" placeholder="输入商品关键词搜索" value="' + escapeHtml(keyword) + '">' +
          '<button type="submit" class="btn btn-primary"><i class="bi bi-search"></i> 查询</button>' +
        '</div>' +
        '<div class="d-flex search-utils">' +
          '<button type="button" class="btn btn-outline-secondary" id="clearKeyword"><i class="bi bi-arrow-counterclockwise"></i> 清空</button>' +
          '<button type="button" class="btn btn-outline-secondary" id="pasteKeyword"><i class="bi bi-clipboard"></i> 粘贴</button>' +
        '</div>' +
      '</form>' +
    '</div></div>' +
    '<div id="streamStatus" class="text-center mb-4">' +
      '<div class="loading-spinner" style="display:inline-block;width:40px;height:40px;border:4px solid #f5f5f5;border-top-color:#1677ff;border-radius:50%;animation:spin 1s linear infinite;"></div>' +
      '<p class="text-secondary mt-2">正在搜索商品...</p>' +
    '</div>' +
    '<div id="streamResults"></div>' +
    '<div id="streamFooter" style="display:none;" class="text-center mt-4">' +
      '<button id="copyAllButton" class="btn btn-secondary btn-lg mb-3"><i class="bi bi-clipboard-data"></i> 复制全部结果文本</button><br>' +
      '<a href="/" class="btn btn-outline-primary btn-lg"><i class="bi bi-house-door"></i> 返回首页</a>' +
    '</div>';

  initSearchForm();
  initClearPasteButtons();

  fetch('/search/stream', {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    body: 'keyword=' + encodeURIComponent(keyword)
  }).then(function(response) {
    if (!response.ok) throw new Error('HTTP ' + response.status);
    var reader = response.body.getReader();
    var decoder = new TextDecoder();
    var buffer = '';

    function pump() {
      return reader.read().then(function(result) {
        if (result.done) {
          onStreamDone();
          return;
        }
        buffer += decoder.decode(result.value, {stream: true});
        var lines = buffer.split('\n');
        buffer = lines.pop();
        var currentEvent = '';
        for (var i = 0; i < lines.length; i++) {
          var line = lines[i];
          if (line.indexOf('event: ') === 0) {
            currentEvent = line.substring(7);
          } else if (line.indexOf('data: ') === 0) {
            var jsonStr = line.substring(6);
            try {
              var data = JSON.parse(jsonStr);
              handleStreamEvent(currentEvent, data);
            } catch(e) {}
            currentEvent = '';
          }
        }
        return pump();
      });
    }

    return pump();
  }).catch(function(err) {
    console.error('Streaming failed:', err);
    showToast('流式加载失败，使用普通查询', 'error');
    window.location.href = '/search?fallback=1';
    var form = document.createElement('form');
    form.method = 'POST';
    form.action = '/search';
    var input = document.createElement('input');
    input.name = 'keyword';
    input.value = keyword;
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
  });
}

function handleStreamEvent(eventType, data) {
  var statusEl = document.getElementById('streamStatus');
  var resultsEl = document.getElementById('streamResults');

  if (eventType === 'search_complete') {
    statusEl.innerHTML =
      '<h2 class="display-6 fw-bold text-brand"><i class="bi bi-check-circle-fill"></i> 查询结果</h2>';
    var skeletons = '';
    for (var s = 0; s < data.total; s++) {
      skeletons += '<div class="card mb-3" id="skeleton-' + (s + 1) + '"><div class="card-body">' +
        '<div class="skeleton-bar" style="width:70%;height:22px;margin-bottom:16px;"></div>' +
        '<div class="row g-3 mb-3">' +
          '<div class="col-sm-6"><div class="skeleton-bar" style="width:40%;height:32px;"></div></div>' +
          '<div class="col-sm-6"><div class="skeleton-bar" style="width:60%;height:18px;"></div></div>' +
        '</div>' +
        '<div class="skeleton-bar" style="width:30%;height:26px;border-radius:20px;margin-bottom:12px;"></div>' +
        '<div class="d-flex gap-2">' +
          '<div class="skeleton-bar" style="width:120px;height:40px;"></div>' +
          '<div class="skeleton-bar" style="width:120px;height:40px;"></div>' +
        '</div>' +
      '</div></div>';
    }
    resultsEl.innerHTML = skeletons;
  } else if (eventType === 'item') {
    var item = data.data;
    var idx = item.index;
    var card = buildItemCard(item, idx);
    var skeleton = document.getElementById('skeleton-' + idx);
    if (skeleton) {
      skeleton.outerHTML = card;
    } else {
      resultsEl.insertAdjacentHTML('beforeend', card);
    }
    initCopyButtons();
  } else if (eventType === 'done') {
    onStreamDone();
  } else if (eventType === 'error') {
    statusEl.innerHTML =
      '<div class="text-center mb-4"><i class="bi bi-info-circle text-brand" style="font-size:4rem;"></i></div>' +
      '<p class="fs-5 text-center text-secondary">' + escapeHtml(data.message) + '</p>';
  }
}

function buildItemCard(item, idx) {
  var tpwdBtn = item.tpwd
    ? '<button class="btn btn-secondary copyTpwdBtn flex-fill" data-tpwd="' + escapeAttr(item.tpwd) + '"><i class="bi bi-clipboard"></i> 复制淘口令</button>'
    : '';
  var linkBtns = item.link_clean
    ? '<a href="taobao://' + escapeAttr(item.link_clean) + '" target="_blank" class="btn btn-success flex-fill"><i class="bi bi-phone"></i> 淘宝 App 打开</a>' +
      '<a href="https://' + escapeAttr(item.link_clean) + '" target="_blank" class="btn btn-info flex-fill"><i class="bi bi-globe"></i> 浏览器打开</a>'
    : '';

  return '<div class="card mb-3"><div class="card-body">' +
    '<div class="result-item slide-up" style="margin-bottom:0;border:none;box-shadow:none;padding:0;">' +
      '<div class="d-flex justify-content-between align-items-start mb-2">' +
        '<h5 class="item-title mb-0"><span class="badge bg-brand rounded-pill me-2">' + idx + '</span>' + escapeHtml(item.title) + '</h5>' +
      '</div>' +
      '<div class="row g-3 mb-3">' +
        '<div class="col-sm-6"><div class="d-flex align-items-center gap-2"><i class="bi bi-currency-yen text-accent fs-4"></i><div><div class="text-secondary small">价格</div><div class="price fw-bold">¥' + escapeHtml(item.price) + '</div></div></div></div>' +
        '<div class="col-sm-6"><div class="d-flex align-items-center gap-2"><i class="bi bi-shop text-brand fs-4"></i><div><div class="text-secondary small">店铺</div><div class="shop-name fw-semibold">' + escapeHtml(item.shop_name) + '</div></div></div></div>' +
      '</div>' +
      '<div class="d-flex justify-content-between align-items-center mb-3"><div class="income-rate"><i class="bi bi-graph-up-arrow"></i> 收入比率: ' + escapeHtml(item.income_rate) + '%</div></div>' +
      '<div class="d-grid gap-2 d-sm-flex justify-content-sm-start button-group">' + tpwdBtn + linkBtns + '</div>' +
    '</div></div></div>';
}

function onStreamDone() {
  var statusEl = document.getElementById('streamStatus');
  var footerEl = document.getElementById('streamFooter');
  var spinner = statusEl.querySelector('.loading-spinner');
  if (spinner) spinner.style.display = 'none';
  var loadingText = statusEl.querySelector('.text-secondary');
  if (loadingText && loadingText.textContent.indexOf('正在加载') !== -1) {
    loadingText.remove();
  }
  if (footerEl) footerEl.style.display = 'block';
  initCopyButtons();
}

function initClearPasteButtons() {
  var clearBtn = document.getElementById('clearKeyword');
  var pasteBtn = document.getElementById('pasteKeyword');
  var keywordInput = document.getElementById('keyword');

  if (clearBtn && keywordInput) {
    clearBtn.onclick = function() {
      keywordInput.value = '';
      keywordInput.focus();
      showToast('已清空', 'info', 1500);
    };
  }

  if (pasteBtn && keywordInput) {
    pasteBtn.onclick = function() {
      if (navigator.clipboard && navigator.clipboard.readText) {
        navigator.clipboard.readText().then(function(text) {
          keywordInput.value = text.trim();
          showToast('已粘贴', 'success', 1500);
        }).catch(function() {
          showToast('无法读取剪贴板内容', 'error');
        });
      } else {
        showToast('浏览器不支持剪贴板功能', 'error');
      }
    };
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

function escapeAttr(str) {
  if (!str) return '';
  return String(str).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/'/g,'&#39;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

/* ========================================
   复制功能增强
   ======================================== */

function initCopyButtons() {
  // 复制单个淘口令按钮
  document.addEventListener('click', function(e) {
    if (e.target.classList.contains('copyTpwdBtn') || e.target.closest('.copyTpwdBtn')) {
      e.preventDefault();
      const button = e.target.classList.contains('copyTpwdBtn') ? e.target : e.target.closest('.copyTpwdBtn');
      const tpwd = button.getAttribute('data-tpwd');

      if (tpwd) {
        copyToClipboard(tpwd, '淘口令已复制到剪贴板！');
      }
    }
  });

  // 复制全部结果按钮
  const copyAllBtn = document.getElementById('copyAllButton');
  if (copyAllBtn) {
    copyAllBtn.addEventListener('click', function() {
      const streamResults = document.getElementById('streamResults');
      const resultElement = document.getElementById('result');
      const source = streamResults || resultElement;
      if (source) {
        copyToClipboard(source.textContent, '结果已复制到剪贴板！');
      }
    });
  }

  // 复制单个结果按钮
  const copyBtn = document.getElementById('copyButton');
  if (copyBtn) {
    copyBtn.addEventListener('click', function() {
      const resultElement = document.getElementById('result');
      if (resultElement) {
        const text = resultElement.textContent;
        copyToClipboard(text, '结果已复制到剪贴板！');
      }
    });
  }
}

/**
 * 复制到剪贴板
 */
function copyToClipboard(text, successMessage = '已复制到剪贴板！') {
  // 现代浏览器使用Clipboard API
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text)
      .then(() => {
        showToast(successMessage, 'success');
      })
      .catch(err => {
        console.error('复制失败:', err);
        fallbackCopyToClipboard(text, successMessage);
      });
  } else {
    // 旧浏览器降级方案
    fallbackCopyToClipboard(text, successMessage);
  }
}

/**
 * 降级复制方案（使用textarea）
 */
function fallbackCopyToClipboard(text, successMessage) {
  const textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.style.position = 'fixed';
  textarea.style.top = '-9999px';
  document.body.appendChild(textarea);
  textarea.select();

  try {
    const successful = document.execCommand('copy');
    if (successful) {
      showToast(successMessage, 'success');
    } else {
      showToast('复制失败，请手动复制', 'error');
    }
  } catch (err) {
    console.error('复制失败:', err);
    showToast('复制失败，请手动复制', 'error');
  }

  document.body.removeChild(textarea);
}

/* ========================================
   加载状态管理
   ======================================== */

function initLoadingState() {
  // 创建加载覆盖层（如果不存在）
  if (!document.querySelector('.loading-overlay')) {
    const overlay = document.createElement('div');
    overlay.className = 'loading-overlay';
    overlay.innerHTML = `
      <div class="loading-spinner"></div>
    `;
    document.body.appendChild(overlay);
  }
}

/**
 * 显示加载状态
 */
function showLoading() {
  const overlay = document.querySelector('.loading-overlay');
  if (overlay) {
    overlay.classList.add('show');
  }
}

/**
 * 隐藏加载状态
 */
function hideLoading() {
  const overlay = document.querySelector('.loading-overlay');
  if (overlay) {
    overlay.classList.remove('show');
  }
}

/* ========================================
   清空和粘贴功能增强
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
  const clearBtn = document.getElementById('clearKeyword');
  const pasteBtn = document.getElementById('pasteKeyword');
  const keywordInput = document.getElementById('keyword');

  if (clearBtn && keywordInput) {
    clearBtn.addEventListener('click', function() {
      keywordInput.value = '';
      keywordInput.focus();
      showToast('已清空', 'info', 1500);
    });
  }

  if (pasteBtn && keywordInput) {
    pasteBtn.addEventListener('click', function() {
      // 检查Clipboard API支持
      if (navigator.clipboard && navigator.clipboard.readText) {
        navigator.clipboard.readText()
          .then(text => {
            keywordInput.value = text.trim();
            showToast('已粘贴', 'success', 1500);
          })
          .catch(err => {
            console.error('粘贴失败:', err);
            showToast('无法读取剪贴板内容', 'error');
          });
      } else {
        showToast('浏览器不支持剪贴板功能', 'error');
      }
    });
  }
});

/* ========================================
   商品卡片动画
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {
  // 为结果项添加进入动画
  const resultItems = document.querySelectorAll('.result-item');
  resultItems.forEach((item, index) => {
    item.style.animationDelay = `${index * 0.1}s`;
    item.classList.add('slide-up');
  });
});

/* ========================================
   工具函数
   ======================================== */

// 防抖函数
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// 节流函数
function throttle(func, limit) {
  let inThrottle;
  return function() {
    const args = arguments;
    const context = this;
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  }
}

/* ========================================
   错误处理
   ======================================== */

window.addEventListener('error', function(e) {
  console.error('页面错误:', e.error);
  showToast('发生了一个错误，请刷新页面重试', 'error');
});

// 未处理的Promise拒绝
window.addEventListener('unhandledrejection', function(e) {
  console.error('未处理的Promise拒绝:', e.reason);
  showToast('操作失败，请重试', 'error');
});