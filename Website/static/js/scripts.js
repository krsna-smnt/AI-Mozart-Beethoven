//Music Status

 var message_span = document.getElementById('MIDIjs.message');
  message_span.innerHTML = MIDIjs.get_audio_status();

  MIDIjs.message_callback = display_status;
  function display_status(message) {
     message_span.innerHTML = message;
  };