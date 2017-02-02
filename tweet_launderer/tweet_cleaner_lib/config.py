BASE_FILE_NAME_UNCLEAN = "tweets"
UNCLEANED_TWEETS_DIRECTORY = "unclean_tweets"

BASE_FILE_NAME_CLEAN = "tweets_ready_for_use"
CLEANED_TWEETS_DIRECTORY = "clean_tweets"

SYMBOLS_TO_DROP = '@#'

STATE_ABBREVIATIONS = {#will convert location to value, allows for multiple ways user may put in location in other words states may have multiple abbreviations so we use value for standardization
	'ALABAMA':'AL',
	'ALASKA':'AK',
	'ARIZONE':'AZ',
	'ARKANSAS':'AR',
	'CALIFORNIA':'CA',
	'COLORADA':'CO',
	'CONNECTICUT':'CT',
	'DELAWARE':'DE',
	'DISTRICT OF COLUMBIA':'DC',
	'FLORIDA':'FL',
	'GEORGIA':'GA',
	'HAWAII':'HI',
	'IDAHO':'ID',
	'ILLINOIS':'IL',
	'INDIANA':'IN',
	'IOWA':'IA',
	'KANSAS':'KS',
	'KENTUCKY':'KY',
	'LOUISIANA':'LA',
	'MAINE':'ME',
	'MARYLAND':'MD',
	'MASSACHUTTES':'MA',
	'MICHIGAN':'MI',
	'MINNESOTA':'MN',
	'MISSISSIPPI':'MS',
	'MISSOURI':'MO',
	'MONTANA':'MT',
	'NEBRASKA':'NE',
	'NEVADA':'NV',
	'NEW HAMPSHIRE':'NH',
	'NEW JERSEY':'NJ',
	'NEW MEXICO':'NM',
	'NEW YORK':'NY',
	'NORTH CAROLINA':'NC',
	'N CAROLINA':'NC',
	'NORTH DAKOTA':'ND',
	'N DAKOTA':'ND',
	'OHIO':'OH',
	'OKLAHOMA':'OK',
	'OREGON':'OR',
	'PENNSYLVANIA':'PA',
	'RHODE ISLAND':'RI',
	'SOUTH CAROLINA':'SC',
	'S CAROLINA':'SC',
	'SOUTH DAKOTA':'SD',
	'S DAKOTA':'SD',
	'TENNESSEE':'TN',
	'TEXAS':'TX',
	'UTAH':'UT',
	'VERMONT':'VT',
	'VIRGINIA':'VA',
	'WASHINGTON':'WA',
	'WEST VIRGINIA':'WV',
	'W VIRGINIA':'WV',
	'WISCONSIN':'WI',
	'WYOMING':'WY'
}

COUNTRY_ABBREVIATIONS = {
	'UNITED STATES':'US',
	'UNITED SATES OF AMERICA':'US',
	'USA':'US',
}
