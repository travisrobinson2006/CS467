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

	$debug = TRUE;//set debugging here, for ease of changing
	if ($debug === TRUE){
		error_reporting(-1);
		ini_set('display_errors', 'On');		
	}

	//set up mysqli connection
	$mysqli = new mysqli("oniddb.cws.oregonstate.edu","robitrav-db","dMD7JvbzBSr4uyHC","robitrav-db");
	if($mysqli->connect_errno)
	{
		echo "Connection error " . $mysqli->connect_errno . " " . $mysqli->connect_error;
	}

	//set default map and map name
	$map_file_path = 'default_images/usa_map.png';
	$map_alt = 'Map of USA';//set alt name of map

	if (htmlspecialchars($_POST['selected_show']) && !$_POST['user_state']){//get whole country data

		if ($debug === TRUE){
			echo "Country View";
		}


		$selected_show = $_POST['selected_show'];
		$selected_show = preg_replace('/\s+/', '', $selected_show);

		if(!($stmt = $mysqli->prepare("SELECT map_file_path FROM country_data WHERE show_name=?"))){
			echo "Prepare failed: "  . $stmt->errno . " " . $stmt->error;
		}

		if(!($stmt->bind_param("s",$selected_show))){
			echo "Bind failed: "  . $stmt->errno . " " . $stmt->error;
		}

		if(!$stmt->execute()){
			echo "Execute failed: "  . $mysqli->connect_errno . " " . $mysqli->connect_error;
		}

		if(!$stmt->bind_result($map_file_path)){
			echo "Bind failed: "  . $mysqli->connect_errno . " " . $mysqli->connect_error;
		}

		while($stmt->fetch()){
//			echo $map_file;
		}

		$stmt->close();

		echo "selected_show: " . htmlspecialchars($_POST['selected_show']) . " ";
		echo "map: " . $map_file_path;
		$map_alt = 'Map of ' . htmlspecialchars($_POST['selected_show']);//set alt name of map
	}

	elseif (htmlspecialchars($_POST['selected_show']) && $_POST['user_state']) {//get individual state data

		if ($debug === TRUE){
			echo "States View";
		}

		$selected_show = $_POST['selected_show'];
		$selected_show = preg_replace('/\s+/', '', $selected_show);

		$user_state = $_POST['user_state'];
		$user_state = preg_replace('/\s+/', '', $user_state);

		if(!($stmt = $mysqli->prepare("SELECT chart_file_path FROM state_data WHERE show_name=?"))){
			echo "Prepare failed: "  . $stmt->errno . " " . $stmt->error;
		}

		if(!($stmt->bind_param("s",$selected_show))){
			echo "Bind failed: "  . $stmt->errno . " " . $stmt->error;
		}

		if(!$stmt->execute()){
			echo "Execute failed: "  . $mysqli->connect_errno . " " . $mysqli->connect_error;
		}

		if(!$stmt->bind_result($chart_file_path)){
			echo "Bind failed: "  . $mysqli->connect_errno . " " . $mysqli->connect_error;
		}

		while($stmt->fetch()){
//			echo $map_file;
		}

		$stmt->close();		

		echo "selected_show: " . htmlspecialchars($_POST['selected_show']) . " ";
		echo "chart: " . $chart_file_path;

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
			<p>
				The following is a map of the United States. To see how Twitter users feel about your favorite (or least favorite!) shows in different areas, enter the show to search for and see how it does!
			</p>

			<?php
				echo '<img id="map_usa" src="' . $map_file_path . '" alt="' . $map_alt . '">'
			?>

			<?php
				if ($chart_file_path){
					echo "The following chart shows your individual states opinion of your selected show.";
					echo '<img src="' . $chart_file_path . '" alt="' . $chart_alt . '">';	
				}

			?>


			<form action="mainpage.php" method="post">
				<fieldset>	
				<legend>See How The Country Feels About Your Show</legend>
					<p>Show Title: 
						<select name="selected_show">
							<?php
								if(!($stmt = $mysqli->prepare("SELECT show_name FROM country_data"))){
									echo "Prepare failed: "  . $stmt->errno . " " . $stmt->error;
								}

								if(!$stmt->execute()){
									echo "Execute failed: "  . $mysqli->connect_errno . " " . $mysqli->connect_error;
								}

								if(!$stmt->bind_result($country_data)){
									echo "Bind failed: "  . $mysqli->connect_errno . " " . $mysqli->connect_error;
								}

								while($stmt->fetch()){
									echo '<option value="'. $country_data . '"> ' . $country_data . '</option>\n';
								}

								$stmt->close();
							?>
						</select>
					</p>

					<p><input type="submit" value="See How My Show Compares!" name="show_whole_country" /></p>
				</fieldset>
			</form>

			<form method="post">
				<fieldset>
					<legend>See How Your State Feels About Your Show</legend>
					<p>
						<label>Show Title: </label>
							<select name="selected_show">
								<?php
									if(!($stmt = $mysqli->prepare("SELECT show_name FROM country_data"))){
										echo "Prepare failed: "  . $stmt->errno . " " . $stmt->error;
									}

									if(!$stmt->execute()){
										echo "Execute failed: "  . $mysqli->connect_errno . " " . $mysqli->connect_error;
									}

									if(!$stmt->bind_result($country_data)){
										echo "Bind failed: "  . $mysqli->connect_errno . " " . $mysqli->connect_error;
									}

									while($stmt->fetch()){
										echo '<option value="'. $country_data . '"> ' . $country_data . '</option>\n';
									}

									$stmt->close();
								?>
							</select>
					</p>
					<p><label>State: </label>
						<select name="user_state">
							<option value="AL">Alabama</option>
							<option value="AK">Alaska</option>
							<option value="AZ">Arizona</option>
							<option value="AR">Arkansas</option>
							<option value="CA">California</option>
							<option value="CO">Colorado</option>
							<option value="CT">Connecticut</option>
							<option value="DE">Delaware</option>
							<option value="DC">District Of Columbia</option>
							<option value="FL">Florida</option>
							<option value="GA">Georgia</option>
							<option value="HI">Hawaii</option>
							<option value="ID">Idaho</option>
							<option value="IL">Illinois</option>
							<option value="IN">Indiana</option>
							<option value="IA">Iowa</option>
							<option value="KS">Kansas</option>
							<option value="KY">Kentucky</option>
							<option value="LA">Louisiana</option>
							<option value="ME">Maine</option>
							<option value="MD">Maryland</option>
							<option value="MA">Massachusetts</option>
							<option value="MI">Michigan</option>
							<option value="MN">Minnesota</option>
							<option value="MS">Mississippi</option>
							<option value="MO">Missouri</option>
							<option value="MT">Montana</option>
							<option value="NE">Nebraska</option>
							<option value="NV">Nevada</option>
							<option value="NH">New Hampshire</option>
							<option value="NJ">New Jersey</option>
							<option value="NM">New Mexico</option>
							<option value="NY">New York</option>
							<option value="NC">North Carolina</option>
							<option value="ND">North Dakota</option>
							<option value="OH">Ohio</option>
							<option value="OK">Oklahoma</option>
							<option value="OR">Oregon</option>
							<option value="PA">Pennsylvania</option>
							<option value="RI">Rhode Island</option>
							<option value="SC">South Carolina</option>
							<option value="SD">South Dakota</option>
							<option value="TN">Tennessee</option>
							<option value="TX">Texas</option>
							<option value="UT">Utah</option>
							<option value="VT">Vermont</option>
							<option value="VA">Virginia</option>
							<option value="WA">Washington</option>
							<option value="WV">West Virginia</option>
							<option value="WI">Wisconsin</option>
							<option value="WY">Wyoming</option>
						</select>
					</p>
					<p><input type="submit" name="show_state" value="See How My Show Compares!"/></p>
				</fieldset>				
			</form>

		</div>










	</body>

</html>