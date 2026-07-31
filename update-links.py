import re

file_path = "/mnt/cos/artifacts/intern-intro.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Project Links
# Project 1: 过程装备智能测控系统 -> https://github.com/zhaotianlina2/chenyuan-portfolio (or we can map them gracefully)
# Let's map Project 1 to: https://github.com/zhaotianlina2/chenyuan-portfolio
# Project 2 to: https://github.com/zhaotianlina2/khalil-fong-music-galaxy
# Project 3 to: https://github.com/zhaotianlina2/khalil-fong-tribute
# Wait, let's use the exact repository names:
# Project 1: chenyuan-portfolio
# Project 2: khalil-fong-music-galaxy
# Project 3: khalil-fong-tribute

# Let's locate the project links section and replace.
# Project 1:
proj1_old = """          <div class="project-links">
            <a href="#" class="project-link primary">查看详情</a>
            <a href="#" class="project-link secondary">省一等奖 🏆</a>
          </div>"""

proj1_new = """          <div class="project-links">
            <a href="https://github.com/zhaotianlina2/chenyuan-portfolio" target="_blank" class="project-link primary">查看仓库</a>
            <a href="https://github.com/zhaotianlina2/chenyuan-portfolio" target="_blank" class="project-link secondary">省一等奖 🏆</a>
          </div>"""

# Project 2:
proj2_old = """          <div class="project-links">
            <a href="#" class="project-link primary">查看详情</a>
            <a href="#" class="project-link secondary">省三等奖</a>
          </div>"""

proj2_new = """          <div class="project-links">
            <a href="https://github.com/zhaotianlina2/khalil-fong-music-galaxy" target="_blank" class="project-link primary">查看仓库</a>
            <a href="https://github.com/zhaotianlina2/khalil-fong-music-galaxy" target="_blank" class="project-link secondary">省三等奖 🥉</a>
          </div>"""

# Project 3:
proj3_old = """          <div class="project-links">
            <a href="#" class="project-link primary">查看详情</a>
            <a href="#" class="project-link secondary">校三等奖</a>
          </div>"""

proj3_new = """          <div class="project-links">
            <a href="https://github.com/zhaotianlina2/khalil-fong-tribute" target="_blank" class="project-link primary">查看仓库</a>
            <a href="https://github.com/zhaotianlina2/khalil-fong-tribute" target="_blank" class="project-link secondary">校三等奖 🥉</a>
          </div>"""

html = html.replace(proj1_old, proj1_new)
html = html.replace(proj2_old, proj2_new)
html = html.replace(proj3_old, proj3_new)


# 2. Update Contact Section to include WeChat Copy-to-Clipboard Button
# Let's add WeChat button before/after mailto or tel.
contact_actions_old = """      <div class="contact-actions reveal">
        <a href="mailto:2233938275@qq.com" class="contact-btn">
          <svg width="20" height="20" fill="none" viewBox="0 0 20 20"><rect x="2" y="4" width="16" height="12" rx="3" stroke="#e95f2b" stroke-width="2"/><path d="M2 7 L10 12 L18 7" stroke="#e95f2b" stroke-width="2" stroke-linecap="round"/></svg>
          发送邮件
        </a>
        <a href="tel:+8618269767181" class="contact-btn">
          <svg width="20" height="20" fill="none" viewBox="0 0 20 20"><path d="M4 3 C4 3 6 3 7 5 L8.5 8 C8.5 8 9 9 8 10 L7 11 C7 11 6.5 11.5 7.5 13 C8.5 14.5 10 16 11.5 17 C13 18 13.5 17.5 13.5 17.5 L14.5 16.5 C15.5 15.5 16.5 16 16.5 16 L19 17.5 C21 18.5 17 21 15 19 C13 17 5 11 3 7 C1 3 4 3 4 3Z" fill="#e95f2b" stroke="#20313a" stroke-width="1.5"/></svg>
          电话联系
        </a>
        <a href="#" class="contact-btn" id="downloadBtn">
          <svg width="20" height="20" fill="none" viewBox="0 0 20 20"><path d="M10 3 L10 13 M6 9 L10 13 L14 9" stroke="#e95f2b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><rect x="3" y="15" width="14" height="2" rx="1" fill="#e95f2b"/></svg>
          下载简历 PDF
        </a>
      </div>"""

contact_actions_new = """      <div class="contact-actions reveal">
        <a href="mailto:2233938275@qq.com" class="contact-btn">
          <svg width="20" height="20" fill="none" viewBox="0 0 20 20"><rect x="2" y="4" width="16" height="12" rx="3" stroke="#e95f2b" stroke-width="2"/><path d="M2 7 L10 12 L18 7" stroke="#e95f2b" stroke-width="2" stroke-linecap="round"/></svg>
          发送邮件
        </a>
        <a href="tel:+8618269767181" class="contact-btn">
          <svg width="20" height="20" fill="none" viewBox="0 0 20 20"><path d="M4 3 C4 3 6 3 7 5 L8.5 8 C8.5 8 9 9 8 10 L7 11 C7 11 6.5 11.5 7.5 13 C8.5 14.5 10 16 11.5 17 C13 18 13.5 17.5 13.5 17.5 L14.5 16.5 C15.5 15.5 16.5 16 16.5 16 L19 17.5 C21 18.5 17 21 15 19 C13 17 5 11 3 7 C1 3 4 3 4 3Z" fill="#e95f2b" stroke="#20313a" stroke-width="1.5"/></svg>
          电话联系
        </a>
        <button class="contact-btn" id="wechatBtn" style="cursor:pointer;border:var(--outline) solid var(--ink);width:100%;text-align:left;outline:none;">
          <svg width="20" height="20" fill="none" viewBox="0 0 20 20" style="margin-right:2px;"><path d="M6 3 C3.5 3 1.5 4.8 1.5 7 C1.5 8.2 2.3 9.3 3.5 10 C3.3 10.7 2.8 11.8 2.5 12.2 C2.3 12.5 2.5 12.5 2.7 12.4 C3.5 12 5 11 5.5 10.7 C5.7 10.8 5.8 10.8 6 10.8 C8.5 10.8 10.5 9 10.5 7 C10.5 4.8 8.5 3 6 3 Z M14 7.5 C12 7.5 10.5 9 10.5 10.8 C10.5 11.1 10.6 11.4 10.8 11.7 C10.3 12.1 9.3 12.8 8.7 13.2 C8.5 13.3 8.6 13.3 8.8 13.2 C9 12.9 9.4 12.2 9.5 11.7 C10.5 11.2 11 10.3 11 9.5 C11 9.4 11 9.2 11 9 C11.8 9.3 12.8 9.5 13.8 9.5 C16 9.5 17.8 8 17.8 6 C17.8 4.2 16 2.8 13.8 2.8 C11.5 2.8 9.8 4.2 9.5 6" stroke="#e95f2b" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          复制微信: ztl18269767181
        </button>
        <a href="#" class="contact-btn" id="downloadBtn">
          <svg width="20" height="20" fill="none" viewBox="0 0 20 20"><path d="M10 3 L10 13 M6 9 L10 13 L14 9" stroke="#e95f2b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><rect x="3" y="15" width="14" height="2" rx="1" fill="#e95f2b"/></svg>
          下载简历 PDF
        </a>
      </div>"""

html = html.replace(contact_actions_old, contact_actions_new)

# 3. Add Toast / Copy JS logic inside the bottom script
# We can find the end of the script before `})();` and insert the Clipboard copy event listener + toast CSS/DOM.
# Let's search for a good insertion point. Let's place it right before `})();`.

clipboard_js = """
    // 3. WeChat Clipboard Copy & Toast Alert
    const wechatBtn = document.getElementById('wechatBtn');
    if (wechatBtn) {
      wechatBtn.addEventListener('click', function() {
        const wechatId = "ztl18269767181";
        navigator.clipboard.writeText(wechatId).then(function() {
          showToast("微信账号 ztl18269767181 已复制到剪贴板！");
        }).catch(function(err) {
          // Fallback
          const tempInput = document.createElement("input");
          tempInput.value = wechatId;
          document.body.appendChild(tempInput);
          tempInput.select();
          try {
            document.execCommand("copy");
            showToast("微信账号 ztl18269767181 已复制到剪贴板！");
          } catch (e) {
            showToast("复制失败，请手动复制: ztl18269767181");
          }
          document.body.removeChild(tempInput);
        });
      });
    }

    function showToast(message) {
      // Check if toast already exists
      let toast = document.getElementById('wechatToast');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'wechatToast';
        toast.style.position = 'fixed';
        toast.style.bottom = '30px';
        toast.style.left = '50%';
        toast.style.transform = 'translateX(-50%) translateY(100px)';
        toast.style.background = '#20313a';
        toast.style.color = '#fffaf2';
        toast.style.padding = '12px 24px';
        toast.style.borderRadius = '8px';
        toast.style.fontWeight = 'bold';
        toast.style.fontFamily = 'var(--ff-body)';
        toast.style.fontSize = '14px';
        toast.style.border = '3px solid var(--ink)';
        toast.style.boxShadow = '4px 4px 0 var(--ink)';
        toast.style.zIndex = '99999';
        toast.style.transition = 'transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        document.body.appendChild(toast);
      }
      toast.innerText = message;
      // Show
      setTimeout(() => {
        toast.style.transform = 'translateX(-50%) translateY(0)';
      }, 50);
      // Hide
      setTimeout(() => {
        toast.style.transform = 'translateX(-50%) translateY(100px)';
      }, 3000);
    }
"""

# Let's find some standard structure to insert before
# For example, before `})();` at the very end of the file.
html_parts = html.split("})();")
if len(html_parts) > 1:
    # Join parts with the clipboard_js added to the second to last part
    html_parts[-2] = html_parts[-2] + clipboard_js
    html = "})();".join(html_parts)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated links and WeChat clipboard function successfully!")
