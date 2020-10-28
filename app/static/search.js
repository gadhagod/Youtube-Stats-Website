function search(){
    
    var s = document.getElementsByName("method")[0];
    var method = s.options[s.selectedIndex].text;
    
    var channel = document.getElementById("channel").value;
    
    document.write("Searching")

    if (method == "Channel ID"){
        window.location.replace("http://yt-stats.herokuapp.com/channel-id/" + channel);
    }
    else{
        window.location.replace("http://yt-stats.herokuapp.com/channel-name/" + channel);
    }
}