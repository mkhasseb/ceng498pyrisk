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
var risk_mapf; // map image file
var risk_state = 'nonne'
	var risk_state_sub = 'none'
		var risk_state_bool = false
		var risk_id; // game id
var risk_selected; // selected/ hovered region
var risk_ws; // world state
var risk_ws_bool = false; // 
var move_from = '';
var move_to = '';
var atack_from = '';
var attack_to = '';
var tool = {
		'x' : 0,
		'y' : 0
}
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
	if ((risk_state == 'roam' || risk_state == 'placeSingle') && risk_map_bool) {

		$.get('adapter.py/map?id=' + risk_id, function(data) {
			if (startsWith(data, "Error")) {
				alert(data)
			} else {
				risk_map = jQuery.parseJSON(data)
				generatePolygons()
				risk_map_bool = false
				risk_ws_bool = true;
			}
		}).error(function(error) {
			if (error.status != 0) {
				alert(error)
			}
		})

		$.get('adapter.py/mapFileName?id=' + risk_id, function(data) {
			if (startsWith(data, "Error")) {
				alert(data)
			} else {

				risk_mapf = new Image()
				risk_mapf.src = data
				mission()
				playername()
				invalidate()
			}
		}).error(function(error) {
			if (error.status != 0) {
				alert(error)
			}
		})
	} else {
		;
	}
}

function generatePolygons() {
	for ( var i = 0; i < risk_map.regions.length; i++) {
		var region = risk_map.regions[i]
		region.center = new Contour(region.points).centroid()
		region.dist = 0
		for ( var k = 0; k < region.points.length; k++) {
			var distance = dist(region.center, region.points[k])
			if (region.dist < distance) {
				region.dist = distance
			}
		}
		region.strokeStyle = "#000000"
			region.draw = function(c) {
			var ccolor = this.continentColor
			c.strokeStyle = this.strokeStyle
			c.lineWidth = 2
			var occolor = this.color
			var grd = c.createRadialGradient(this.center.x, this.center.y, 1,
					this.center.x, this.center.y, this.dist);
			grd.addColorStop(0, occolor)
			// grd.addColorStop(0.26, occolor)
			grd.addColorStop(0.3, "#FFFFFF")
			// grd.addColorStop(0.5, ccolor)
			grd.addColorStop(1, ccolor)
			c.fillStyle = grd
			c.beginPath()

			c.moveTo(this.points[0].x, this.points[0].y)
			for ( var j = 1; j < this.points.length; j++) {
				var p = this.points[j]
				c.lineTo(p.x, p.y)
			}
			c.closePath()
			c.fill()
			c.stroke()
			c.font = "bold 12px sans-serif";
			c.fillStyle = '#000000'
				c.fillText(this.name + " " + this.armies, this.center.x - 35,
						this.center.y)

		}
	}
}

function dist(p1, p2) {
	return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2))
}

function getState() {
	if(risk_state_bool){
		$.get('adapter.py/state?id=' + risk_id, function(data) {
			if (startsWith(data, "Error")) {
				risk_state_bool = false
				alert(data)
			} else {
				risk_state_bool = false
				risk_state = data
				$("#stateSpan").text(risk_state)
				if (risk_state == "defend") {
					var diceNum = ""
						while (diceNum == null || diceNum == "") {
							diceNum = prompt("Please enter army number", "1");
						}
					defend(diceNum)
				}
				if(risk_state == 'transferarmies'){
					var diceNum = ""
						while (diceNum == null || diceNum == "") {
							diceNum = prompt("Please enter armies to transfer", "1");
						}
					transfer(diceNum)	
				}
				if(risk_state == 'attack' || risk_state == 'trade' || risk_state == 'moveorpass' || risk_state == 'placeIncome' ){
					$("#passButton").removeClass("invisible")
				}else if(risk_state == 'transferarmies' || risk_state == 'roam' || risk_state == 'placeArmies' || risk_state == 'placeSingle'){
					$("#passButton").addClass("invisible")
				}
				if(risk_state == 'trade'){
					$("#tradeButton").removeClass("invisible")
				}else{
					$("#tradeButton").addClass("invisible")
				}
				

				risk_state_bool = true

			}
		}).error(function(error) {
			if (error.status != 0) {
				risk_state_bool = false
				alert(error)
			}
		})
	}
}

function getWs() {
	if (risk_ws_bool) {
		$.get('adapter.py/worldMap?id=' + risk_id, function(data) {
			if (startsWith(data, "Error")) {

			} else {
				risk_ws = jQuery.parseJSON(data)
				for ( var i = 0; i < risk_ws.regions.length; i++) {
					var reg = risk_ws.regions[i]
					for ( var j = 0; j < risk_map.regions.length; j++) {
						var r = risk_map.regions[j]
						if (r.name == reg.name) {
							r.color = reg.occupant
							r.armies = reg.armyNum
							break;
						}
					}
				}
				risk_ws_bool = true
				invalidate()
			}
		}).error(function(error) {
			if (error.status != 0) {
				risk_ws_bool = false
				alert(error)
				risk_ws_bool = true
			}
		})
	}
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
var WIDTH = 900;
var HEIGHT = 700;

function draw() {
	if (!canvasValid && risk_map) {
		clear(context)
		if (risk_mapf) {
			context.drawImage(risk_mapf, 0, 0)
		}
		for ( var i = 0; i < risk_map.regions.length; i++) {
			var region = risk_map.regions[i]
			if (region.draw) {
				region.draw(context)
			}
		}
		canvasValid = true

	}

}

function enableGame() {
	$("#game").removeClass("invisible")
	$("#serverConn").addClass("invisible")
	$("#gamesTable").addClass("invisible")
	init()
	risk_map_bool = true;
	risk_state_bool = true;
	setInterval("draw()", 20)
	setInterval("getState()", 1000)
	setInterval("getMap()", 1000)
	setInterval("getLog()", 1000)
	setInterval("getWs()", 1000)
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
	canvas.addEventListener('mousemove', ev_mousemove, false);
	// canvas.addEventListener('mousedown', ev_mousedown, false);
	canvas.addEventListener('mouseup', ev_mouseup, false);
}

function coords(ev) {

	// Get the mouse position relative to the canvas element.
	if (ev.layerX || ev.layerX == 0) { // Firefox
		tool.x = ev.layerX;
		tool.y = ev.layerY;
	} else if (ev.offsetX || ev.offsetX == 0) { // Opera
		tool.x = ev.offsetX;
		tool.y = ev.offsetY;
	}

}

function ev_mousemove(ev) {
	coords(ev)
	getSelected()
	invalidate()
}

function ev_mouseup(ev) {
	coords(ev)
	getSelected()
	invalidate()

	if (risk_selected) {
		// $("#attackButton").addClass("invisible")
		if (risk_state == 'placeSingle') {
			risk_state_sub = 'placeSingle'
				placeSingle(risk_selected.name)
		} else if (risk_state == 'placeArmies') {
			risk_state_sub = 'placeArmies'
				var armyNum = ""
					while (armyNum == null || armyNum == "") {
						armyNum = prompt("Please enter army number", "1");
					}
			var placeArmyStr = risk_selected.name + ',' + armyNum
			placeArmies(placeArmyStr)
		} else if (risk_state == 'placeIncome') {
			risk_state_sub = 'placeIncome'
				var armyNum = ""
					while (armyNum == null || armyNum == "") {
						armyNum = prompt("Please enter army number", "1");
					}
			var placeIncomeStr = risk_selected.name + ',' + armyNum
			placeIncome(placeIncomeStr)
			$("#passButton").removeClass("invisible")
		} else if (risk_state == 'attack') {
			if (risk_state_sub == 'attack1') {
				attack_to = risk_selected.name
				risk_state_sub = 'attack2'
					var diceNum = ""
						while (diceNum == null || diceNum == "") {
							diceNum = prompt("Please enter army number", "1");
						}
				var attackStr = attack_from + ',' + attack_to + ',' + diceNum
				attack(attackStr)
				attack_from = ''
					attack_to = ''
						$("#passButton").removeClass("invisible")
			}else{
				attack_from = risk_selected.name
				risk_state_sub = 'attack1'
				$("#passButton").addClass("invisible")
			}
		} else if (risk_state == 'move0') {
			if (risk_state_sub == 'move1') {
				move_to = risk_selected.name
				risk_state_sub = 'move2'
					var armyNum = ""
						while (armyNum == null || armyNum == "") {
							armyNum = prompt("Please enter army number", "1");
						}
				var moveStr = move_from + ',' + move_to + ',' + armyNum
				move(moveStr)
				move_from = ''
					move_to = ''
						$("#passButton").removeClass("invisible")
			}else{
				move_from = risk_selected.name
				risk_state_sub = 'move1'
				$("#passButton").addClass("invisible")
			}
		}
	}
}

function pass(ev) {
	$.get('adapter.py/doPass?id=' + risk_id, function(data) {
		if (startsWith(data, "Error")) {
			alert(data)
		} else {
			$("#passButton").addClass("invisible")
			$("#tradeButton").addClass("invisible")
			risk_state_sub = "roam"
		}
	}).error(function(error) {
		if (error.status != 0) {
			alert(error)
		}
	})
}

function placeSingle(rname) {
	$.get('adapter.py/placeSingle?id=' + risk_id + '&name=' + rname,
			function(data) {
		if (startsWith(data, "Error")) {
			alert(data)
		}
	}).error(function(error) {
		if (error.status != 0) {
			alert(error)
		}
	})
}

function defend(diceNum) {
	$.ajax({ 
		url: 'adapter.py/defend?id=' + risk_id + '&diceNum=' + diceNum,
		async: false
	})
}

function transfer(armyNum) {
	$.ajax({ 
		url: 'adapter.py/transfer?id=' + risk_id + '&armyNum=' + armyNum,
		async : false
	})

}

function placeArmies(placeArmyStr) {
	$.get(
			'adapter.py/placeArmy?id=' + risk_id + '&placeArmyStr='
			+ placeArmyStr, function(data) {
				if (startsWith(data, "Error")) {
					alert(data)
				}
			}).error(function(error) {
				if (error.status != 0) {
					alert(error)
				}
			})
}

function placeIncome(placeIncomeStr) {
	$.get(
			'adapter.py/placeIncome?id=' + risk_id + '&placeIncomeStr='
			+ placeIncomeStr, function(data) {
				if (startsWith(data, "Error")) {
					alert(data)
				}
			}).error(function(error) {
				if (error.status != 0) {
					alert(error)
				}
			})
}

function mission() {
	$.get('adapter.py/mission?id=' + risk_id,
			function(data) {
		if (startsWith(data, "Error")) {
			alert(data)
		}else{
			$("#mission").text(data)
		}
	}).error(function(error) {
		if (error.status != 0) {
			alert(error)
		}
	})
}

function playername() {
	$.get('adapter.py/playername?id=' + risk_id ,
			function(data) {
		if (startsWith(data, "Error")) {
			alert(data)
		}else{
			$("#playername").attr("style", 'background-color: ' + data)
		}
	}).error(function(error) {
		if (error.status != 0) {
			alert(error)
		}
	})
}

function attack(attackStr) {
	$.get('adapter.py/attack?id=' + risk_id + '&attackStr=' + attackStr,
			function(data) {
		if (startsWith(data, "Error")) {
			alert(data)
		}
	}).error(function(error) {
		if (error.status != 0) {
			alert(error)
		}
	})
}

function move(moveStr) {
	$.get('adapter.py/move?id=' + risk_id + '&moveStr=' + moveStr,
			function(data) {
		if (startsWith(data, "Error")) {
			alert(data)
		} else {

		}
	}).error(function(error) {
		if (error.status != 0) {
			alert(error)
		}
	})
}



function getSelected() {
	clear(gctx)
	if (risk_map) {
		for ( var i = 0; i < risk_map.regions.length; i++) {
			var region = risk_map.regions[i]
			region.draw(gctx)
			var imageData = gctx.getImageData(tool.x, tool.y, 1, 1);
			if (imageData.data[3] > 0) {
				risk_selected = region
				risk_selected.strokeStyle = "#FF0000"
					return
			}
			clear(gctx)
		}
	}
	if (risk_selected) {
		risk_selected.strokeStyle = "#000000"
			risk_selected = undefined
	}
	return
}

function clear(context) {
	context.clearRect(0, 0, WIDTH, HEIGHT)
}

function invalidate() {
	canvasValid = false
}

function Point(x, y) {
	this.x = x;
	this.y = y;
}

// Contour object
function Contour(points) {
	this.pts = points || []; // an array of Point objects defining the
	// contour
}

Contour.prototype.area = function() {
	var area = 0;
	var pts = this.pts;
	var nPts = pts.length;
	var j = nPts - 1;
	var p1;
	var p2;

	for ( var i = 0; i < nPts; j = i++) {
		p1 = pts[i];
		p2 = pts[j];
		area += p1.x * p2.y;
		area -= p1.y * p2.x;
	}
	area /= 2;

	return area;
};

Contour.prototype.centroid = function() {
	var pts = this.pts;
	var nPts = pts.length;
	var x = 0;
	var y = 0;
	var f;
	var j = nPts - 1;
	var p1;
	var p2;

	for ( var i = 0; i < nPts; j = i++) {
		p1 = pts[i];
		p2 = pts[j];
		f = p1.x * p2.y - p2.x * p1.y;
		x += (p1.x + p2.x) * f;
		y += (p1.y + p2.y) * f;
	}

	f = this.area() * 6;

	return new Point(x / f, y / f);
};
