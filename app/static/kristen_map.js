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
						fill: "white",
					},
					attrsHover: {
						fill: "white",
					},
				},
			},
		},
		plots: {
			hunan: {
				latitude: 27.583584,
				longitude: 111.699844,
				tooltip: { content: "HuNan, China" },
			},

			guangxi: {
				latitude: 23.787529,
				longitude: 108.77496,
				tooltip: { content: "GuangXi, China" },
			},

			ontario: {
				latitude: 42.986897,
				longitude: -81.246216,
				tooltip: { content: "London, Ontario" },
			},

		},
		// Links allow you to connect plots between them
		links: {
			guangxiontario: {
				// ... Or with IDs of plotted points
				factor: -0.6,
				between: ["guangxi", "hunan"],
				attrs: {
					"stroke-width": 2,
				},
			},

			hunanontario: {
				// ... Or with IDs of plotted points
				factor: -0.6,
				between: ["hunan", "ontario"],
				attrs: {
					"stroke-width": 2,
				},
			},
		},
	});
});
