// Displays the element ID in the URL, and automatically opens the related modal if you navigate directly to the ID of the card


// Displays the ID ofthe card in the URL
function changeURL(e){
  var hash = e.currentTarget.id;
  window.location.hash = "#modal" + hash;
}

function getHashFromCards(){
  var cards = document.querySelectorAll('.card');
  for (i = 0; i < cards.length; i++) {
    cards[i].addEventListener("click", changeURL);
  }
}
getHashFromCards();


// Opens the modal on page load
function openModal(){
  var location = window.location.hash.substring(6);
  console.log(location);
  if (location != "") {
    var modal = "course-" + location + "-modal";
    $("#" + modal).foundation("open");
  }
}
openModal();
