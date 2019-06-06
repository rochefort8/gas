window.onload = function() {
  
  var val = 6 ;
  
  var off_y = val * 80;
  var bottom_y = off_y + 80;
  var margin_top_y = 176 - off_y;
  
  cssRules =  document.styleSheets.item( 0 ).cssRules;
  style = cssRules.item (0).style;
  style.setProperty( 'clip' , 'rect(' + off_y + 'px,80px,' + bottom_y + 'px, 0px)' );
  style.setProperty( 'margin-top' , margin_top_y + 'px'  );
}
