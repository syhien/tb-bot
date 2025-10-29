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

  // 表单提交处理
  searchForm.addEventListener('submit', function(e) {
    const keyword = searchInput.value.trim();

    if (!keyword) {
      e.preventDefault();
      showToast('请输入搜索关键词', 'error');
      searchInput.focus();
      return;
    }

    // 显示加载状态
    showLoading();
  });

  // 输入框回车事件
  searchInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      searchForm.dispatchEvent(new Event('submit'));
    }
  });
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
      const resultElement = document.getElementById('result');
      if (resultElement) {
        const text = resultElement.textContent;
        copyToClipboard(text, '结果已复制到剪贴板！');
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