window.onload = function() {
  
  val = getParam('value')
  if (val != null) {
    setValue(val)
  }
}
  
function setValue(val) {  
  var digit = 9 ;
  var prev = val % 10 ;
  
  for (  var i = 0;  i <7;  i++  ) {
    val = val / 10;
    digit = parseInt(val % 10);
    var off_y = digit * 50 + 5 * prev;
      
    if (digit != 9) {
      prev = 0;
    } 
    var bottom_y = off_y + 50;
    var margin_top_y = 121 - off_y;
    
    cssRules =  document.styleSheets.item( 0 ).cssRules;
    style = cssRules.item (6-i).style;
    style.setProperty( 'clip' , 'rect(' + off_y + 'px,80px,' + bottom_y + 'px, 0px)' );
    style.setProperty( 'margin-top' , margin_top_y + 'px'  );
  }
}

function getParam(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}