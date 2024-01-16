import Song from models;

$("#favorite").onclick(function() {
    var song = Song.objects.get(api_id=id);
    if (song.favorite == False) song.favorite = True;
    else song.favorite = False;
    song.save();
    alert("Favorites edited.");
});

$(".btn btn-primary").onclick = function() {
    var id = this.id;
    var song = Song.objects.get(api_id=id);
    if (song.favorite == False) song.favorite = True;
    else song.favorite = False;
    song.save();
    alert("Favorites edited.");
};