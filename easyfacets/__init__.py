# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import pandas as pd
from IPython.core.display import display, HTML
from easyfacets.generic_feature_statistics_generator import GenericFeatureStatisticsGenerator
import base64

# Create Facets template  
HTML_TEMPLATE = """<link rel="import" href="/nbextensions/facets-dist/facets-jupyter.html">
        <facets-dive sprite-image-width="{sprite_size}" sprite-image-height="{sprite_size}" id="elem" height="600"></facets-dive>
        <script>
          document.querySelector("#elem").data = {jsonstr};
        </script>"""

# Load the json dataset and the sprite_size into the template
def visualize_facets_dive(df):
    sprite_size = 32 if len(df.index)>50000 else 64
    jsonstr = df.to_json(orient='records')
    html = HTML_TEMPLATE.format(jsonstr=jsonstr, sprite_size=sprite_size)
    return display(HTML(html))

def visualize_facets_overview(df):
    proto = GenericFeatureStatisticsGenerator().ProtoFromDataFrames([{'name': 'test', 'table': df}])
    protostr = base64.b64encode(proto.SerializeToString()).decode("utf-8")
    HTML_TEMPLATE = """<link rel="import" href="/nbextensions/facets-dist/facets-jupyter.html" >
        <facets-overview id="elem"></facets-overview>
        <script>
          document.querySelector("#elem").protoInput = "{protostr}";
        </script>"""
    html = HTML_TEMPLATE.format(protostr=protostr)
    return display(HTML(html))