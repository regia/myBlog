var ListingDialog = {
  wrapper: document.createElement('div'),
  init : function() {
  },

  insert : function() {
    var f = document.forms[0], textarea_output, options = '';

    //If no code just return.
    if(f.mtext.value == '') {
      tinyMCEPopup.close();
      return false;
    }
    f.mtext.value = f.mtext.value.replace(/</g,'&lt;'); 
    f.mtext.value = f.mtext.value.replace(/>/g,'&gt;'); 
    textarea_output = '<pre><code'; 
    if (f.mlanguage.value == 'auto') {
    textarea_output += '>'; 
    }
    else {
    textarea_output += ' class="' + f.mlanguage.value + '">'; 
    };
    textarea_output += f.mtext.value; 
    textarea_output += '</code></pre> ';

	this.wrapper.innerHTML = textarea_output;
	hljs.highlightBlock(this.wrapper.firstChild.firstChild, '    ');
	tinyMCEPopup.editor.execCommand('mceInsertContent', false, this.wrapper.innerHTML);
	tinyMCEPopup.close();
  }
};
tinyMCEPopup.onInit.add(ListingDialog.init, ListingDialog);
