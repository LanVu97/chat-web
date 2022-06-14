
// We define a variable 'text_box' for storing the html code structure of message that is displayed in the chat box.
var text_box = '<div class="card-panel right" style="width: 75%; position: relative" id="id">' +
    '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
    '{message}' +
    '</div>';

function send(sender_id, receiver_id, message) {
    $.post('/chat/send/', {
        sender: sender_id,
        receiver: receiver_id,
        message: message,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    }, function (data) {
        console.log(data);
        var box = text_box.replace('{sender}', "You");
        box = box.replace('{message}', message); // Replace the text '{message}' with the message that has been sent.
        // console.log(box)
        $('#board').append(box); // Render the message inside the chat-box by appending it at the end.

        scrolltoend();

    })
};


function receive() {

    $.ajax({
        type: 'GET',
        // 'sender_id' and 'receiver_id' are global variable declared in the messages.html, which contains the ids of the users.
        url: "/chat/get_message_new/" + sender_id + "/" + receiver_id,
        success: function (data) {
            // console.log(data);
            if (data.length !== 0) {

                for (var key in data.messages) {

                    var box = text_box.replace('{sender}', sender_username);
                    box = box.replace('{message}', data.messages[key].message);
                    box = box.replace('right', 'left blue lighten-5');
                    $('#board').append(box);
                    scrolltoend();
                }
            }

        },
        // error: function (response) {
        //     alert('An error occured')
        // }
    });

}

function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 800);
}

