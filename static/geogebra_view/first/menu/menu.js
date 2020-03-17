$(document).ready(function() {
  var menu = $("#mini-menu-container");
  let menu_width = menu.width();
  let transfer_right = 1.05 * menu_width;
  let transfer_top = 1.15 * menu_width;
  var input = document.getElementById("menu-open");
  var menu_is_open = false;

  function open_menu() {
    menu.animate({ left: "-=" + transfer_right, top: "-=" + transfer_top });
    input.checked = true;
    menu_is_open = true;
  }

  function close_menu() {
    menu.animate({ left: "+=" + transfer_right, top: "+=" + transfer_top });
    input.checked = false;
    menu_is_open = false;
  }

  menu.toggle(open_menu, close_menu);

});
