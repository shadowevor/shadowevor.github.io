function GenerateCharacter(race_id)
{
	$.ajax({
		type: "POST",
		url: "/htmlgen.py",
		success: function(msg){
			alert("Hi!"+msg);
		}
	}
}
