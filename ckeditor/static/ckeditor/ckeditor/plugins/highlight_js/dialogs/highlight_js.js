CKEDITOR.dialog.add( 'highlight_js', function( editor ) {
    return {
        title: editor.lang.highlight_js.highlight.dialogTitle,
        minWidth: 800,
        minHeight: 500,
        contents: [
            {
                id: 'tab-basic',
                label: 'Basic Settings',
                elements: [
                    {
                        type: 'select',
                        id: 'code_lan',
                        label: editor.lang.highlight_js.highlight.selectLabel,
                        items: [
                                [ 'Auto' ],
                                [ 'no-highlight' ],
                                [ 'Bash' ],
                                [ 'Diff' ],
                                [ 'JSON' ],
                                [ 'C#', 'cs' ],
                                [ 'HTML', 'xml' ],
                                [ 'XML', 'xml' ],
                                [ 'JAVA' ],
                                [ 'Python' ],
                                [ 'C++', 'cpp' ],
                                [ 'HTTP' ],
                                [ 'JavaScript' ],
                                [ 'Ruby' ],
                                [ 'CSS' ],
                                [ 'PHP' ],
                                [ 'ini' ],
                                [ 'SQL' ],
                                [ 'Perl' ],
                                [ " 1C " ],
                                [ "AVR Assembler", 'avrasm"' ],
                                [ "ActionScript" ],
                                [ "Apache" ],
                                [ "AppleScript" ],
                                [ "Axapta" ],
                                [ "Brainfuck" ],
                                [ "CMake" ],
                                [ "Clojure" ],
                                [ "CoffeeScript" ],
                                [ "D" ],
                                [ "DOS .bat", 'dos'],
                                [ "Delphi" ],
                                [ "Django" ],
                                [ "Erlang" ],
                                [ "OpenGL Shading Language", 'glsl' ],
                                [ "Go" ],
                                [ 'Haskell' ],
                                [ "Lisp" ],
                                [ "Lua" ],
                                [ "MEL" ],
                                [ "Markdown" ],
                                [ "Matlab" ],
                                [ "Nginx" ],
                                [ "Objective C", 'objectivec' ],
                                [ "Parser3" ],
                                [ "Python profile", 'profile' ],
                                [ "R" ],
                                [ "RenderMan RIB", 'rib"' ],
                                [ "RenderMan RSL", 'rsl' ],
                                [ "Rust" ],
                                [ "Scala" ],
                                [ "Smalltalk" ],
                                [ "TeX" ],
                                [ "VBScript" ],
                                [ "VHDL" ],
                                [ "Vala" ]
                              ],
                        'default': 'Auto',
                        onChange: function( api ) {
                        // this = CKEDITOR.ui.dialog.select
                         //alert( 'Current value: ' + this.getValue() );
                        }
                    },
                    {
                        type: 'textarea',
                        id: 'pre_code',
                        rows: 22,
                        style: "width: 100%"
                        /*setup: function(data) {
                            if (data.code)
                                this.setValue(data.code);
                        },
                        commit: function(data) {
                            data.code = this.getValue();
                        }*/
                    }
                ]
            }

        ],
        onOk: function() {
            var dialog = this;

            var pre = editor.document.createElement( 'pre' );
            var code = editor.document.createElement( 'code' );
            var code_class = dialog.getValueOf( 'tab-basic', 'code_lan' ).toLowerCase();

            if(code_class !== "auto"){
                code.setAttribute( 'class', code_class );
            }

            code.setText( dialog.getValueOf( 'tab-basic', 'pre_code' ) );

            pre.append(code);

            editor.insertElement(pre);
        }
    };
});
