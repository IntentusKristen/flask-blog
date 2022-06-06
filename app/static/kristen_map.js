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
				tooltip: { content: "GuangXi, China" },
			},
			ontario: {
				latitude: 52.00401,
				longitude: -91.754666,
				tooltip: { content: "London, Ontario" },
			},

		},
		// Links allow you to connect plots between them
		links: {
			chinaontario: {
				// ... Or with IDs of plotted points
				factor: -0.6,
				between: ["china", "ontario"],
				attrs: {
					"stroke-width": 2,
				},
			},
		},
	});
});
