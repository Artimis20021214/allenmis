/*
 * main.js
 * 負責頁面互動功能，包括右側選單的彈出與關閉，以及基本滾動效果
 */
(function($) {
  "use strict";

  // 當頁面與所有資源載入完畢後移除 "is-preload"
  $(window).on('load', function() {
    $('body').removeClass('is-preload');
  });

  // 右下角浮動按鈕事件監聽：開啟右側選單
  $('#openSideMenu').on('click', function(e) {
    e.preventDefault();
    $('#sideMenuModal').fadeIn(); // 使用淡入效果顯示選單
  });

  // 選單內關閉按鈕事件監聽：關閉選單
  $('#sideMenuModal .close-btn').on('click', function(e) {
    e.preventDefault();
    $('#sideMenuModal').fadeOut(); // 使用淡出效果隱藏選單
  });

  // 點擊選單外部背景時：關閉選單
  $('#sideMenuModal').on('click', function(e) {
    if (e.target === this) { // 確保點擊的是背景層
      $(this).fadeOut();
    }
  });

  // 菜單項目平滑滾動效果
  $('#menu ul li a').on('click', function(e) {
    var target = $(this).attr('href'); // 獲取連結的目標位置
    if (target.charAt(0) === '#') { // 判斷是否為 hash 連結
      e.preventDefault();
      var $target = $(target);
      if ($target.length) {
        $('html, body').animate({
          scrollTop: $target.offset().top
        }, 800); // 平滑滾動至目標區塊
      }
    }
  });

  // 滾動事件：可以新增區塊特效或條件式功能（可選）
  $(window).on('scroll', function() {
    // 偵測滾動高度，可用於實現固定導航或其他互動功能
    var scrollTop = $(window).scrollTop();
    if (scrollTop > 200) {
      $('#openSideMenu').addClass('active'); // 例如讓按鈕有特效
    } else {
      $('#openSideMenu').removeClass('active');
    }
  });

})(jQuery);