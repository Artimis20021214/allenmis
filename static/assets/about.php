<!DOCTYPE html>
<html lang="zh-TW">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>張予綸簡介</title>
	<style type="text/css">
		* { font-family:"標楷體"; margin-left:auto; margin-right:auto;}
		h1 {color:blue; font-size:60px;}
		h2 {color:#33ff33; font-size:40px;}
	</style>
	<script>
		function change1() {
			document.getElementById("pic").src = "mountain.jpg";
			document.getElementById("h2text").innerText = "靜宜資管";
		}

		function change2() {
			document.getElementById("pic").src = "cliff.jpg";
			document.getElementById("h2text").innerText = "Yu-Lun Zhung";
		}
	</script>
</head>
<body>
	<table width="70%">
		<tr>
			<td>
				<img src="cliff.jpg" width="110%" id="pic"
				onmouseover="change1()" onmouseout="change2()"></img>
			</td>

			<td>
				<h1>張予綸</h1>
				<h2 id="h2text">yu-lun zhung</h2>
			</td>
		</tr>
	</table>
		<table width="70%"border="1">
			<tr>
				<td>
					FB:<a href="https://reurl.cc/26pDVX" target="_blank">https://www.facebook.com/profile</a><br>
					E-Mail:<a href="mailto:artmis20021214@gmail.com">artmis20021214@gmail.com</a><br>
				</td>
				<td>
					電影配樂<br>
					<audio controls>
						<source src="elephant.mp3" type="audio/mP3">
					</audio><br>
				</td>

				<td>
					不要去臺灣<br>
					<iframe src="https://www.youtube.com/embed/pW88QFpHXa8" allowfullscreen></iframe>
				</td>
				<td>
					<iframe
					allow="microphone;"
					width="350"
					height="430"
					src="https://console.dialogflow.com/api-client/demo/embedded/07aecc9c-7a7c-49d9-8e4a-2575d17dd1ce">
					</iframe>
				</td>
			</tr>
		</table>
	<?php echo date("Y-m-d") ?>
</body>
</html>