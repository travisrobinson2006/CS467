<!--
Travis Robinson
Rohan Gokhale
Chase Hu
CS457
Online Capstone Project
Winter 2017
mainpage.php
-->


<?php

	//set file paths here
	$scales_path = 'scales' . '/';
	$red_green_path = $scales_path . 'red_yellow_green_scale.png';
	$image_path = 'images' . '/';
	$state_images_dir = $image_path . 'state_show_sentiments' . '/';
	$country_maps_dir = $image_path . 'show_maps' . '/';
	$country_state_comps = $image_path . 'state_comp_by_show' . '/';
	$default_map_file_path = 'default_images/usa_map.png';

	$debug = TRUE;//set debugging here, for ease of changing
	if ($debug === TRUE){
		error_reporting(-1);
		ini_set('display_errors', 'On');		
	}

	//set default map and map name
	$map_file_path = $default_map_file_path;
	$map_alt = 'Map of USA';//set alt name of map

	if (htmlspecialchars($_POST['selected_show'])){//get whole country data
		if ($debug === TRUE){
			echo "Country View";
			echo " selected_show: " . htmlspecialchars($_POST['selected_show']) . " ";
			echo "map: " . $map_file_path;
		}

		$selected_show = $_POST['selected_show'];
		$map_file_path = $country_maps_dir . $selected_show;
		$map_alt = 'Map of ' . htmlspecialchars($_POST['selected_show']);//set alt name of map
	}

	elseif ($_POST['user_state']) {//get individual state data

		if ($debug === TRUE){
			echo "States View";
			echo "chart: " . $chart_file_path;
		}

		$user_state = $_POST['user_state'];
		$chart_file_path = $state_images_dir . $user_state;
		$chart_alt = 'Chart of ' . htmlspecialchars($_POST['user_state']);
	}

	else {//get default 'no data' page

		if ($debug === TRUE){
			echo "Default Page View--No User Input";
		}		
	}
?>

<html>
	<head>
		<title>Centaurus: Group Capstone Project</title>
		<link rel="stylesheet" type="text/css" href="mainpage_styles.css">
	</head>

 	<body>
		<?php if ($debug === TRUE) : ?>
			<h2 class = "debug">Debug ON</h2>
			<p class = "debug">
				This page is a work in progress, and the quality of it should be understood to be as such
			</p>
		<?php endif; ?>

		<div class="center">
			<h1>Centaurus: Twitter Sentiment Visualization</h1>

			<?php
				if($map_file_path !== $default_map_file_path){
					echo "The following map shows how each State across the mainland US feels about " . pathinfo($selected_show)['filename'] . " (Hawaii and Alaska not included in this map";
				}
				else{
					echo "This is the default map of the US. To see how a favorite show compares across the country, or, to see how your State feels about several different shows, select from one of the drop down menus below";
				}
				echo '<br><img id="map_usa" src="' . $map_file_path . '" alt="' . $map_alt . '">';

				if($map_file_path !== $default_map_file_path){
					echo '<br><img src="' . $red_green_path . '" alt="' . $map_alt . '"><br>';
					echo '<br>The following chart shows how ' . pathinfo($selected_show)['filename'] . ' compares across the US, on a scale of 1 to 10, with 10 being the highest sentiment';
					echo '<br><img id="map_usa" src="' . $country_state_comps . $selected_show . '" alt="' . $map_alt . '">';
				}

				if ($chart_file_path){
					echo "<br>The following bar chart shows the sentiment score of " . pathinfo($user_state)['filename'] . " for all shows in the study. Shows are graded on a scale from 1 to 10, with 10 being the highest sentiment.<br>";
					echo '<br><img id="map_usa" src="' . $chart_file_path . '" alt="' . $chart_alt . '">';	
				}

			?>

			<p>
				To see how Twitter users feel about your favorite (or least favorite!) shows in different States across the country, select your show from the drop down menu, and see how it does!
			</p>

			<form action="mainpage.php" method="post">
				<fieldset>	
				<legend>See How The Country Feels About Your Show</legend>
					<p>Show Title: 
						<select name="selected_show">
							<?php
								$maps_array =  array_slice(scandir($country_maps_dir, SCANDIR_SORT_ASCENDING),2);
								foreach ($maps_array as $key => $value) {
									echo '<option value="' . $value . '">' . pathinfo($value)['filename'] . '</option>';
								}								
							?>
						</select>
					</p>

					<p><input type="submit" value="See How My Show Compares!" name="show_whole_country" /></p>
				</fieldset>
			</form>

			<p>
				To see how Twitter users in your State feel about all shows, select your state from the drop-down menu and below.
			</p>

			<form method="post">
				<fieldset>
					<legend>See How Your State Feels About Your Show</legend>
					<p><label>State: </label>
						<select name="user_state">
						<?php 
							$state_charts_array =  array_slice(scandir($state_images_dir, SCANDIR_SORT_ASCENDING),2);
							foreach ($state_charts_array as $key => $value) {
								echo '<option value="' . $value . '">' . pathinfo($value)['filename'] . '</option>';
							}
						 ?>
						</select>
					</p>
					<p><input type="submit" name="show_state" value="See How My Show Compares!"/></p>
				</fieldset>				
			</form>
		</div>

		<?php //Source: http://bl.ocks.org/NPashaP/a74faf20b492ad377312
			echo '<div id="tooltip"></div><!-- div to hold tooltip. -->
				<svg width="960" height="600" id="statesvg"></svg> <!-- svg to hold the map. -->
				<script src="uStates.js"></script> <!-- creates uStates. -->
				<script src="http://d3js.org/d3.v3.min.js"></script>
				<script>

					function tooltipHtml(n, d){	/* function to create html content string in tooltip div. */
						return "<h4>"+n+"</h4><table>"+
							"<tr><td>Sentiment Score</td><td>"+(d.sentiment_score)+"</td></tr>"+
							"</table>";
					}
					
					var sampleData ={};	/* Sample random data. */	
					["HI", "AK", "FL", "SC", "GA", "AL", "NC", "TN", "RI", "CT", "MA",
					"ME", "NH", "VT", "NY", "NJ", "PA", "DE", "MD", "WV", "KY", "OH", 
					"MI", "WY", "MT", "ID", "WA", "DC", "TX", "CA", "AZ", "NV", "UT", 
					"CO", "NM", "OR", "ND", "SD", "NE", "IA", "MS", "IN", "IL", "MN", 
					"WI", "MO", "AR", "OK", "KS", "LS", "VA"]
						.forEach(function(d){ 
							var sentiment_score=Math.round(10*Math.random());
							sampleData[d]={sentiment_score:sentiment_score,color:d3.interpolate("#ffffcc", "#800026")(sentiment_score/10)}; 
						});
					
					/* draw states on id #statesvg */	
					uStates.draw("#statesvg", sampleData, tooltipHtml);
					
					d3.select(self.frameElement).style("height", "600px"); 
				</script>';
		 ?>






	</body>
</html>