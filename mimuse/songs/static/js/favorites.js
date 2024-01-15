import Song from models;

$('#favorite').click(function() {
    var song = Song.objects.get(api_id=id);
    if (song.favorite == False) song.favorite = True;
    else song.favorite = False;
    song.save();
});