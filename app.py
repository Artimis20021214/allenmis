from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>個人簡介</title>
    <style>
        /* 整體背景與字體設定 */
        body {
            background-color: #041E42;
            color: white;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        /* 頁首區塊 */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
        }
        /* 左上角的圖示 */
        .logo {
            font-size: 24px;
            font-weight: bold;
        }
        /* 右上角的選單按鈕 */
        .menu {
            font-size: 24px;
            cursor: pointer;
        }
        /* 主內容容器 */
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 40px;
        }
        /* 分段區塊 */
        .section {
            margin-bottom: 40px;
        }
        .section h1, .section h2 {
            margin-bottom: 10px;
        }
        /* 分隔線效果 */
        .section h2 {
            border-bottom: 1px solid #fff;
            padding-bottom: 5px;
        }
        /* Modal（彈出視窗）容器 */
        .modal {
            display: none; /* 預設隱藏 */
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0, 0.5); /* 半透明黑色背景 */
        }
        /* Modal 內容 */
        .modal-content {
            background-color: #3B5998;
            margin: 15% auto;
            padding: 20px;
            border: 1px solid #888;
            width: 80%;
            max-width: 400px;
            position: relative;
            border-radius: 5px;
        }
        /* 關閉按鈕 */
        .close {
            color: white;
            position: absolute;
            top: 10px;
            right: 15px;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }
        .modal-content ul {
            list-style: none;
            padding: 0;
        }
        .modal-content li {
            padding: 10px;
            border-bottom: 1px solid #fff;
        }
        .modal-content li:last-child {
            border-bottom: none;
        }
    </style>
</head>
<body>
    <!-- 頁首 -->
    <div class="header">
        <div class="logo">◆</div>
        <div class="menu" id="menuBtn">≡</div>
    </div>

    <!-- 主內容 -->
    <div class="container">
        <div class="section">
            <h1>個人簡介</h1>
            <p>這裡是你的個人簡介內容，可以簡單介紹自己、興趣、經歷等訊息。</p>
        </div>
        <div class="section">
            <h2>基本資料</h2>
            <p>這裡是你的基本資料，例如姓名、年齡、聯絡方式等。</p>
        </div>
    </div>

    <!-- Modal 結構 -->
    <div id="myModal" class="modal">
      <div class="modal-content">
        <span class="close" id="closeModal">&times;</span>
        <h2>MENU</h2>
        <ul>
          <li>個人簡介</li>
          <li>我的測驗結果</li>
          <li>MIS工作分析</li>
          <li>求職歷程</li>
        </ul>
      </div>
    </div>

    <!-- JavaScript 控制彈出視窗 -->
    <script>
        // 取得相關的元素
        var modal = document.getElementById("myModal");
        var menuBtn = document.getElementById("menuBtn");
        var closeModal = document.getElementById("closeModal");

        // 點擊選單按鈕顯示彈出視窗
        menuBtn.onclick = function() {
            modal.style.display = "block";
        }

        // 點擊關閉按鈕隱藏彈出視窗
        closeModal.onclick = function() {
            modal.style.display = "none";
        }

        // 點擊 Modal 以外的區域也會關閉視窗
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)



if __name__ == '__main__':
    app.run(debug=True)