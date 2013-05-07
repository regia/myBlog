(function() {
    //tinymce.PluginManager.requireLangPack('lstng');
    tinymce.create('tinymce.plugins.ListingPlugin', {
        init : function(ed, url) {
        this.editor = ed;
            ed.addCommand('mceListing', function() {

                ed.windowManager.open({
                    file: url + '/dialog.htm',
                    width: 500,
                    height: 400,
                    inline: 1
                }, {
                    plugin_url : url
                    //some_custom_arg : 'custom arg'
                });


            });

           ed.addButton('lstng', {
                title: 'Вставка кода',
                cmd: 'mceListing',
                image: url + '/img/example.gif'
           });

           //ed.addShortcut('ctrl+k', false, 'mceListing');

            ed.onNodeChange.add(function(ed, cm, n) {
                cm.setActive('lstng', n.nodeName == 'IMG');
            });

          },

           createControl : function(n, cm) {
               return null;
           },

          getInfo : function() {
           return {
            longname : 'Listing Plugin',
            author: 'Owlman',
            authorurl: 'http://owlman.net/',
            version: "1.0"
           };
          }
     });


   tinymce.PluginManager.add('lstng', tinymce.plugins.ListingPlugin);
})();
