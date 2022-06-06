$(function () {
	$(".mapcontainer").mapael({
		map: {
			name: "world_countries",
			defaultArea: {
				attrs: {
					fill: "#2a283e",
					stroke: "#56526e",
				},
				attrsHover: {
					fill: "#44415a",
				},
			},
			// Default attributes can be set for all links
			defaultLink: {
				factor: 0.4,
				attrs: {
					stroke: "#C4A7E7",
					opacity: 0.5,
				},
				attrsHover: {
					stroke: "#C4A7E7",
				},
			},
			defaultPlot: {
				text: {
					attrs: {
						fill: "#E0DEF4",
					},
					attrsHover: {
						fill: "#E0DEF4",
					},
				},
			},
		},
		plots: {
			philippines: {
				latitude: 13.735705,
				longitude: 121.066404,
				tooltip: { content: "Philippines" },
			},
			canada: {
				latitude: 52.00401,
				longitude: -91.754666,
				tooltip: { content: "Canada" },
			},
			california: {
				latitude: 37.792032,
				longitude: -122.394613,
				tooltip: { content: "California" },
			},
			kansascity: {
				latitude: 39.096356,
				longitude: -94.578748,
				tooltip: {
					content: "Kansas City",
				},
			},
			colorado: {
				latitude: 38.982987,
				longitude: -105.401174,
				tooltip: { content: "Colorado" },
			},
		},
		// Links allow you to connect plots between them
		links: {
			philippinescalifornia: {
				// ... Or with IDs of plotted points
				factor: -0.3,
				between: ["philippines", "california"],
				attrs: {
					"stroke-width": 1,
				},
			},
			californiacanada: {
				factor: -0.8,
				between: ["california", "canada"],
				attrs: {
					"stroke-width": 1,
				},
			},
			californiakansascity: {
				factor: -0.5,
				between: ["california", "kansascity"],
				attrs: {
					"stroke-width": 1,
				},
			},
			kansascitycolorado: {
				factor: 0.1,
				between: ["kansascity", "colorado"],
				attrs: {
					"stroke-width": 1,
				},
			},
		},
	});
});
