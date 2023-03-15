function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    const input = document.querySelector('#screenshot-upload');
    input.files = [file];
}

function handleDragOver(event) {
    event.preventDefault();
}