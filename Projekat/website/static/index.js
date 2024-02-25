function  deleteNote(noteId){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({ notesId: noteId })
    }).then((_res) => {
        window.location.href = "/";
    })
}