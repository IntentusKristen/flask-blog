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
			china: {
				latitude: 32.049999,
				longitude: 118.766670,
				tooltip: { content: "Nanjing, China" },
			},
			ontario: {
				latitude: 52.00401,
				longitude: -91.754666,
				tooltip: { content: "Mississauga, Ontario" },
			},
            alberta: {
				latitude: 51.049999,
				longitude: -114.066666,
				tooltip: { content: "Calgary, Alberta" },
			},
            vancouver: {
				latitude: 49.246292,
				longitude: -123.116226,
				tooltip: { content: "Vancouver, British Colombia" },
			},
			california: {
				latitude: 37.792032,
				longitude: -122.394613,
				tooltip: { content: "Los Angeles, California" },
			},
			florida: {
				latitude: 27.994402,
				longitude: -81.760254,
				tooltip: {
					content: "Maimi, Florida",
				},
			},
		},
		// Links allow you to connect plots between them
		links: {
			chinavancouver: {
				// ... Or with IDs of plotted points
				factor: -0.6,
				between: ["china", "vancouver"],
				attrs: {
					"stroke-width": 2,
				},
			},
			vancouverontario: {
				factor: -0.8,
				between: ["vancouver", "ontario"],
				attrs: {
					"stroke-width": 2,
				},
			},
			ontarioalberta: {
				factor: -0.5,
				between: ["ontario", "alberta"],
				attrs: {
					"stroke-width": 2,
				},
			},
			albertaontario: {
				factor: 0.1,
				between: ["alberta", "ontario"],
				attrs: {
					"stroke-width": 2,
				},
            },
            ontariofl: {
                factor: 0.1,
                between: ["ontario", "florida"],
                attrs: {
                    "stroke-width": 2,
                },
            },
            ontariocalifornia: {
                factor: 0.1,
                between: ["ontario", "california"],
                attrs: {
                    "stroke-width": 2,
                },
			},
		},
	});
});