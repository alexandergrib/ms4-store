tinymce.init({
    selector: '.tinymce',
    menubar: 'edit view format insert table help',
    toolbar: 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | forecolor backcolor| bullist numlist outdent indent | link image | preview |  emoticons',

    plugins: [
        'advlist autolink link image lists charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'table emoticons template paste help'
    ],

    menu: {
        edit: {title: 'Edit', items: 'undo redo | cut copy paste | selectall | searchreplace'},
        view: {
            title: 'View',
            items: 'code | visualaid visualchars visualblocks | spellchecker | preview fullscreen'
        },
        format: {
            title: 'Format',
            items: 'bold italic underline strikethrough superscript subscript codeformat | formats blockformats fontformats fontsizes align lineheight | forecolor backcolor | removeformat'
        },

        insert: {
            title: 'Insert',
            items: 'image link media template codesample inserttable | charmap emoticons hr | pagebreak nonbreaking anchor toc | insertdatetime'
        },
        table: {title: 'Table', items: 'inserttable | cell row column | tableprops deletetable'},
    },
    help: {title: 'Help', items: 'help'},
    height: 500,
    minHeight: 300,
});
