# svg Tutorials

| Attribute   | Purpose                                     |
| ----------- | ------------------------------------------- |
| `r`         | The radius of the circle                    |
| `cx`        | The x position of the center of the circle  |
| `cy`        | The y position of the center of the circle  |
| `rx`        | The x radius of the ellipse                 |
| `ry`        | The y radius of the ellipse                 |

## Circle

<svg>
  <circle cx="60" cy="60" r="50" stroke="black" stroke-width="2" fill="silver"/>
</svg>

```svg
<svg>
  <circle cx="60" cy="60" r="50" stroke="black" stroke-width="2" fill="silver"/>
</svg>
```

## Rectangle

<svg id="squareID">
  <rect x="10" y="10" width="100" height="100" stroke="darkgrey" fill="transparent" stroke-width="5"/>
</svg>

```svg
<svg id="squareID">
  <rect x="10" y="10" width="100" height="100" stroke="darkgrey" fill="transparent" stroke-width="5"/>
</svg>
```

## Ellipse

<svg id="ellipseID">
  <ellipse cx="75" cy="75" rx="70" ry="50" stroke="#a6a6a6" fill="transparent" stroke-width="5"/>
</svg>

```svg
<svg id="ellipseID">
  <ellipse cx="75" cy="75" rx="70" ry="50" stroke="#a6a6a6" fill="transparent" stroke-width="5"/>
</svg>
```

## Line

<svg id="lineID">
  <line x1 = "20" y1 = "20" x2 = "175" y2 = "180" stroke = "black" stroke-width = "3"/>
</svg>

```svg
<svg id="lineID">
  <line x1 = "20" y1 = "20" x2 = "175" y2 = "180" stroke = "black" stroke-width = "3"/>
</svg>
```

## Polyline

<svg id="polylineID">
  <polyline points = "20,20 40,25 60,40 80,120 120,140 200,180" fill = "none" stroke = "black" stroke-width = "3"/>
</svg>

```svg
<svg id="polylineID">
  <polyline points = "20,20 40,25 60,40 80,120 120,140 200,180" fill = "none" stroke = "black" stroke-width = "3"/>
</svg>
```

## Polygon

<svg id="polygonID">
   <polygon points = "60,10 140,10 190,70 190,130 140,190 70,190 10,130 10,70" fill = "gainsboro" stroke = "black" stroke-width = "3"/>
</svg>

```svg
<svg id="polygonID">
   <polygon points = "60,10 140,10 190,70 190,130 140,190 70,190 10,130 10,70" fill = "gainsboro" stroke = "black" stroke-width = "3"/>
</svg>
```

## sandbox

### axis

<svg id="testID">
  <line x1 = "0" y1 = "0" x2 = "0" y2 = "180" stroke = "black" stroke-width = "3"/>
  <line x1 = "0" y1 = "0" x2 = "180" y2 = "0" stroke = "black" stroke-width = "3"/>
</svg>

<br>

### cartesian

<svg width="220" height="220" xmlns="http://www.w3.org/2000/svg">
  <!-- Draw X and Y axes -->
  <line x1="10" y1="110" x2="210" y2="110" stroke="black" stroke-width="2"/> <!-- X-axis -->
  <line x1="110" y1="10" x2="110" y2="210" stroke="black" stroke-width="2"/> <!-- Y-axis -->

  <!-- Draw X-axis ticks -->
  <line x1="60" y1="105" x2="60" y2="115" stroke="black" stroke-width="2"/>  <!-- Left tick -->
  <line x1="160" y1="105" x2="160" y2="115" stroke="black" stroke-width="2"/> <!-- Right tick -->

  <!-- Draw Y-axis ticks -->
  <line x1="105" y1="60" x2="115" y2="60" stroke="black" stroke-width="2"/>  <!-- Top tick -->
  <line x1="105" y1="160" x2="115" y2="160" stroke="black" stroke-width="2"/> <!-- Bottom tick -->

</svg>

