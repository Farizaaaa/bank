$(function(){
    $('#groups').on('change', function(){
        var val = $(this).val();
        var sub = $('#sub_groups');
        $('option', sub).filter(function(){
            if (
                 $(this).attr('data-group') === val
              || $(this).attr('data-group') === 'SHOW'
            ) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
    $('#groups').trigger('change');
});




















//
//
//
//var subjectObject = {
//  "Front-end": {
//    "HTML": ["Links", "Images", "Tables", "Lists"],
//    "CSS": ["Borders", "Margins", "Backgrounds", "Float"],
//    "JavaScript": ["Variables", "Operators", "Functions", "Conditions"]
//  },
//  "Back-end": {
//    "PHP": ["Variables", "Strings", "Arrays"],
//    "SQL": ["SELECT", "UPDATE", "DELETE"]
//  }
//}
//window.onload = function() {
//  var subjectSel = document.getElementById("subject");
//  var topicSel = document.getElementById("topic");
//  var chapterSel = document.getElementById("chapter");
//  for (var x in subjectObject) {
//    subjectSel.options[subjectSel.options.length] = new Option(x);
//  }
//  subjectSel.onchange = function() {
//    //empty Chapters- and Topics- dropdowns
//    chapterSel.length = 1;
//    topicSel.length = 1;
//    //display correct values
//    for (var y in subjectObject[this.value]) {
//      topicSel.options[topicSel.options.length] = new Option(y);
//    }
//  }
//  topicSel.onchange = function() {
//    //empty Chapters dropdown
//    chapterSel.length = 1;
//    //display correct values
//    var z = subjectObject[subjectSel.value][this.value];
//    for (var i = 0; i < z.length; i++) {
//      chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
//    }
//  }
//}