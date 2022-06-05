
```{python}
import pandas as pd
import numpy as np
from kmodes.kmodes import KModes
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import json
```



fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.show()




fig = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


```{r display_plotly_plot}

plotly::as_widget(
  jsonlite::fromJSON(
    reticulate::py$fig, simplifyVector=FALSE))
```
