<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>readcsv.php</title>
</head>
<body>
	<h1>TWEETS</h1>
	<div>
 		<?php
			print "
				<table border = '1'>
					<tr>
						<th>Tweet</th>
						<th>Username</th>
						<th>Promo</th>
					</tr>
			";
			$data = file("integrated_data/integrated_with_label.csv");
			foreach ($data as $line){
				print 	"<tr>
							<td> '$line' </td>
						<tr>";
						#<tr>
					#		<td> '$line[1]' </td>
					#	<tr>
					#	<tr>
					#		<td> '$line[2]' </td>
					#	<tr>";
			} // end foreach
			//print the bottom of the table
			print "</table>";
		?>
	</div>
</body>
</html>