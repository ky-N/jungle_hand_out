$(document).ready(function () {
                $("#cards-box").html("");
                showArticles();
            });

function postMemo() {
    $.ajax({
        type: "POST",
        url: "/memo_create",
        data: {post_Title: $("input#post_Title").val(), post_Body: $("input#post_Body").val()},
        success: function (response) { // 성공하면
            if (response["result"] == "success") {
                alert(response["msg"]);
            }
        }
    })
}

function showArticles() {
    $.ajax({
        type: "GET",
        url: "/memo",
        data: {},
        success: function (response) {
            if (response["result"] == "success") {
                alert(response["msg"]);
            }
        }
    })
}

function makeCard(url, title, desc, comment, image) {

}