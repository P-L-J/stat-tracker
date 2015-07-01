function svgGraph(id){

var svg = d3.select("svg");

var g = svg.append("g");
g.attr("transform", "translate(100,50)");

var gx = g.append("g")
gx.attr("transform", "translate(0,400)");

function getDate(d) {
    return new Date(d);
}

var x = d3.time.scale()
    .domain([getDate("2015-06-01"), getDate("2015-07-01")])
    .range([0, 800]);
var y = d3.scale.linear()
    .domain([0, 20])
    .range([400, 0]);

var y_axis = d3.svg.axis().scale(y).orient("left").ticks(4);
g.call(y_axis);

var x_axis = d3.svg.axis().scale(x).orient("bottom").ticks(5).tickFormat(d3.time.format("%m/%Y"));
gx.call(x_axis);

d3.json('/api/activities/' + id, function(data) {
  g.selectAll("circle")
      .data(data["stat_set"])
    .enter().append("circle")
      .attr("cx", function(d) {return x(getDate(d["date"]));} )
      .attr("cy", function(d) {return y(d["value"]);} )
      .attr("r", 10);

});

}
