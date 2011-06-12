/**
 * 
 */
// global vars all prefixed by risk_
var risk_phost; // host for proxy server
var risk_pport; // port for proxy server
var risk_ptry = false; // whether try proxy server connection
var risk_gamestat; // game list from server
var risk_map; // game map
var risk_map_bool = false;
var risk_state = 'nonne'
var risk_state_bool = false
var risk_id; // game id
// Connects proxy server and retrieves
function risk_connect_proxy() {
	if (risk_ptry) {
		risk_ptry = false
		$.get(
				'adapter.py/serverstatus?host=' + risk_phost + "&port="
						+ risk_pport, function(data) {
					if (!startsWith(data, "Error")) {
						risk_gamestat = jQuery.parseJSON(data)
						updateGamesTable()
						risk_ptry = true
					} else {
						$("#gamesTable").addClass("invisible")
						alert(data)
					}
				}).error(function(error) {
			if (error.status != 0) {
				alert(error)
				$("#gamesTable").addClass("invisible")
			}
		})
	} else {
		; // do nothing
	}
}

function getMap() {
	if(risk_state == 'roam' && risk_map_bool){
		$.get('adapter.py/map?id=' + risk_id, function(data) {
			if (startsWith(data, "Error")) {
				alert(data)
			} else {
				risk_map = jQuery.parseJSON(data)
				risk_pols = generatePolygons()
				risk_map_bool = false
			}
		}).error(function(error) {
			if (error.status != 0) {
				alert(error)
			}
		})
	}else{
		;
	}
}

function generatePolygons(){
	for(var i=0; i < risk_map.regions.length){
		risk_map.regions.draw = function(c){
			
		}
	}
}

function getState() {
	$.get('adapter.py/state?id=' + risk_id, function(data) {
		if (startsWith(data, "Error")) {
			risk_state_bool = false
			alert(data)
		} else {
			risk_state_bool = true
			risk_state = data
		}
	}).error(function(error) {
		if (error.status != 0) {
			risk_state_bool = false
			alert(error)
		}
	})
}

function getLog() {
	$.get('adapter.py/log?id=' + risk_id, function(data) {
		if (startsWith(data, "Error")) {
			alert(data)
		} else {
			$("#log")[0].value = data
		}
	}).error(function(error) {
		if (error.status != 0) {
			alert(error)
		}
	})
}

function join(addr) {
	var l = addr.split(':')
	$.get('adapter.py/join?host=' + l[0] + "&port=" + l[1], function(data) {
		if (startsWith(data, "Error")) {
			risk_ptry = true
			alert(data)
		} else {
			risk_ptry = false
			risk_id = jQuery.parseJSON(data).id
			enableGame()
		}
	}).error(function(error) {
		if (error.status != 0) {
			alert(error)
		}
	})
}

function startsWith(str, suffix) {
	return str.match("^" + suffix) == suffix
}

function updateGamesTable() {
	$("#gamesTable").removeClass("invisible")
	var body = $("#itsthetable tbody")
	var d = document
	body.empty()

	for ( var key in risk_gamestat) {
		if (risk_gamestat.hasOwnProperty(key)) {
			var val = risk_gamestat[key]

			var row = d.createElement("tr")

			var th = d.createElement("th")
			th.innerHTML = val["name"]
			row.appendChild(th)

			var addr = d.createElement("td")
			addr.innerHTML = val["address"]
			row.appendChild(addr)

			var players = d.createElement("td")
			players.innerHTML = val["players"]
			row.appendChild(players)

			var buttontd = d.createElement("td")
			var button = d.createElement("button")
			var span = d.createElement("span")

			button.setAttribute("role", "button")
			button.setAttribute("aria-disabled", "false")
			button.setAttribute("onclick", "javascript: join('"
					+ val['address'] + "')")
			span.setAttribute("class", "ui-button-text")

			var l = val["players"].split("/")
			l[0] = l[0].match("[0,1,2,3,4,5,6]")[0]
			l[1] = l[1].match("[0,1,2,3,4,5,6]")[0]
			var full = ((parseInt(l[0])) === (parseInt(l[1])))
			if (full) {
				span.innerHTML = "Full"
				button
						.setAttribute(
								"class",
								"button-disabled ui-button ui-widget ui-state-inactive ui-corner-all ui-button-text-only ")
			} else {
				button
						.setAttribute(
								"class",
								"button-enabled ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only")
				span.innerHTML = "Join"
			}
			button.appendChild(span)
			buttontd.appendChild(button)
			row.appendChild(buttontd)
			body[0].appendChild(row)

		}
	}
	buttons()
}

function risk_update_proxy() {
	risk_phost = $("#host")[0].value
	risk_pport = $("#port")[0].value
	risk_ptry = true
}

function buttons() {
	// hover states on the static widgets
	$('#dialog_link, ul#icons li, .button-enabled').hover(function() {
		$(this).addClass('ui-state-hover');
	}, function() {
		$(this).removeClass('ui-state-hover');
	});

}
$(document).ready(function() {
	setInterval("risk_connect_proxy()", 1000)
	buttons()
	risk_phost = $("#host")[0].value = 'localhost'
	risk_pport = $("#port")[0].value = '8090'
})

// /Canvas part
var canvas;
var canvasValid = false;
var context;
var ghostcanvas;
var WIDTH = 500;
var HEIGHT = 500;

function enableGame() {
	$("#game").removeClass("invisible")
	$("#serverConn").addClass("invisible")
	$("#gamesTable").addClass("invisible")
	init()
	risk_map_bool = true;
	// setInterval("draw()", 20)
	setInterval("getState()", 1000)
	setInterval("getMap()", 1000)
	setInterval("getLog()", 1000)
	getMap()
}

function init() {

	canvas = document.getElementById('view');
	if (!canvas) {
		alert('Error: I cannot find the canvas element!');

	}

	if (!canvas.getContext) {
		alert('Error: no canvas.getContext!');

	}

	// Get the 2D canvas context.
	context = canvas.getContext('2d');
	if (!context) {
		alert('Error: failed to getContext!');

	}

	ghostcanvas = document.createElement('canvas');
	ghostcanvas.height = HEIGHT;
	ghostcanvas.width = WIDTH;
	gctx = ghostcanvas.getContext('2d');

	// Attach the mousemove event handler.
	// canvas.addEventListener('mousemove', ev_mousemove, false);
	// canvas.addEventListener('mousedown', ev_mousedown, false);
	// canvas.addEventListener('mouseup', ev_mouseup, false);
}