{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "ur8xi4C7S06n"
   },
   "outputs": [],
   "source": [
    "# Copyright 2025 Google LLC\n",
    "#\n",
    "# Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "#     https://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JAPoU8Sm5E6e"
   },
   "source": [
    "# Prompt Design - Best Practices\n",
    "\n",
    "<table align=\"left\">\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/intro_prompt_design.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://www.gstatic.com/pantheon/images/bigquery/welcome_page/colab-logo.svg\" alt=\"Google Colaboratory logo\"><br> Open in Colab\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://console.cloud.google.com/vertex-ai/colab/import/https:%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fprompts%2Fintro_prompt_design.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://lh3.googleusercontent.com/JmcxdQi-qOpctIvWKgPtrzZdJJK-J3sWE1RsfjZNwshCFgE_9fULcNpuXYTilIR2hjwN\" alt=\"Google Cloud Colab Enterprise logo\"><br> Open in Colab Enterprise\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https://raw.githubusercontent.com/GoogleCloudPlatform/generative-ai/main/gemini/prompts/intro_prompt_design.ipynb\">\n",
    "      <img src=\"https://www.gstatic.com/images/branding/gcpiconscolors/vertexai/v1/32px.svg\" alt=\"Vertex AI logo\"><br> Open in Workbench\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/intro_prompt_design.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://www.svgrepo.com/download/217753/github.svg\" alt=\"GitHub logo\"><br> View on GitHub\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://goo.gle/4fWHlze\">\n",
    "      <img width=\"32px\" src=\"https://cdn.qwiklabs.com/assets/gcp_cloud-e3a77215f0b8bfa9b3f611c0d2208c7e8708ed31.svg\" alt=\"Google Cloud logo\"><br> Open in  Cloud Skills Boost\n",
    "    </a>\n",
    "  </td>\n",
    "</table>\n",
    "\n",
    "<div style=\"clear: both;\"></div>\n",
    "\n",
    "<b>Share to:</b>\n",
    "\n",
    "<a href=\"https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/intro_prompt_design.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg\" alt=\"LinkedIn logo\">\n",
    "</a>\n",
    "<a href=\"https://bsky.app/intent/compose?text=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/intro_prompt_design.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/7/7a/Bluesky_Logo.svg\" alt=\"Bluesky logo\">\n",
    "</a>\n",
    "<a href=\"https://twitter.com/intent/tweet?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/intro_prompt_design.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/5/5a/X_icon_2.svg\" alt=\"X logo\">\n",
    "</a>\n",
    "<a href=\"https://reddit.com/submit?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/intro_prompt_design.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://redditinc.com/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png\" alt=\"Reddit logo\">\n",
    "</a>\n",
    "<a href=\"https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/prompts/intro_prompt_design.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg\" alt=\"Facebook logo\">\n",
    "</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "84f0f73a0f76"
   },
   "source": [
    "| Authors |\n",
    "| --- |\n",
    "| [Polong Lin](https://github.com/polong-lin) |\n",
    "| [Karl Weinmeister](https://github.com/kweinmeister) |"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "tvgnzT1CKxrO"
   },
   "source": [
    "## Overview\n",
    "\n",
    "This notebook covers the essentials of prompt engineering, including some best practices.\n",
    "\n",
    "Learn more about prompt design in the [official documentation](https://cloud.google.com/vertex-ai/docs/generative-ai/text/text-overview).\n",
    "\n",
    "In this notebook, you learn best practices around prompt engineering -- how to design prompts to improve the quality of your responses.\n",
    "\n",
    "This notebook covers the following best practices for prompt engineering:\n",
    "\n",
    "- Be concise\n",
    "- Be specific and well-defined\n",
    "- Ask one task at a time\n",
    "- Turn generative tasks into classification tasks\n",
    "- Improve response quality by including examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "61RBz8LLbxCR"
   },
   "source": [
    "## Getting Started"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "No17Cw5hgx12"
   },
   "source": [
    "### Install Google Gen AI SDK\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "tFy3H3aPgx12"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install --upgrade --quiet google-genai"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "06489bd14f16"
   },
   "source": [
    "### Import libraries\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "154137022fb6"
   },
   "outputs": [],
   "source": [
    "from IPython.display import Markdown, display\n",
    "from google import genai\n",
    "from google.genai.types import GenerateContentConfig"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "DF4l8DTdWgPY"
   },
   "source": [
    "### Set Google Cloud project information and create client\n",
    "\n",
    "To get started using Vertex AI, you must have an existing Google Cloud project and [enable the Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com).\n",
    "\n",
    "Learn more about [setting up a project and a development environment](https://cloud.google.com/vertex-ai/docs/start/cloud-environment)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "id": "Nqwi-5ufWp_B"
   },
   "outputs": [],
   "source": [
    "import os\n",
    "\n",
    "PROJECT_ID = \"qwiklabs-gcp-04-54b844aee9a4\"\n",
    "LOCATION = os.environ.get(\"GOOGLE_CLOUD_REGION\", \"global\")\n",
    "\n",
    "client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "OnFPpCRtXRl4"
   },
   "source": [
    "### Load model\n",
    "\n",
    "Learn more about all [Gemini models on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models#gemini-models)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "id": "IQYu_9SvXQah"
   },
   "outputs": [],
   "source": [
    "MODEL_ID = \"gemini-2.5-flash\"  # @param {type: \"string\"}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "cVOtUNJ5X0PY"
   },
   "source": [
    "## Prompt engineering best practices"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "uv_e0fEPX60q"
   },
   "source": [
    "Prompt engineering is all about how to design your prompts so that the response is what you were indeed hoping to see.\n",
    "\n",
    "The idea of using \"unfancy\" prompts is to minimize the noise in your prompt to reduce the possibility of the LLM misinterpreting the intent of the prompt. Below are a few guidelines on how to engineer \"unfancy\" prompts.\n",
    "\n",
    "In this section, you'll cover the following best practices when engineering prompts:\n",
    "\n",
    "* Be concise\n",
    "* Be specific, and well-defined\n",
    "* Ask one task at a time\n",
    "* Improve response quality by including examples\n",
    "* Turn generative tasks to classification tasks to improve safety"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0pY4XX0OX9_Y"
   },
   "source": [
    "### Be concise"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "xlRpxyxGYA1K"
   },
   "source": [
    "🛑 Not recommended. The prompt below is unnecessarily verbose."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "YKV4G-CfXdbi"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "That's a lovely niche! Focusing on dried flowers evokes a sense of longevity, timelessness, nostalgia, and rustic charm. Here are some name ideas, categorized by their vibe, to get your creativity flowing:\n",
       "\n",
       "**I. Elegant & Timeless:**\n",
       "These names suggest sophistication and enduring beauty.\n",
       "\n",
       "1.  **The Everlasting Bloom:** Classic, direct, and conveys permanence.\n",
       "2.  **Heirloom Hues:** Implies vintage beauty and something to be cherished.\n",
       "3.  **Botanical Endures:** Sophisticated, focuses on the plant life and its lasting nature.\n",
       "4.  **Still Life Florals:** Evokes an artistic, composed beauty, like a painting.\n",
       "5.  **Petal & Endure:** A chic, two-word option.\n",
       "6.  **The Enduring Stem:** Simple, elegant, and highlights the structure.\n",
       "7.  **Eternity Blooms:** A slightly more poetic take on everlasting.\n",
       "8.  **The Preserved Petal:** Clear and elegant.\n",
       "\n",
       "**II. Rustic & Whimsical:**\n",
       "These names hint at natural charm, warmth, and a touch of magic.\n",
       "\n",
       "9.  **Dried & True:** A playful take on \"tried and true,\" suggesting reliability and natural beauty.\n",
       "10. **Whispering Blooms:** Suggests quiet beauty and stories held within the flowers.\n",
       "11. **Sun-Kissed Stems:** Evokes the natural drying process and warmth.\n",
       "12. **The Fading Bloom Co. (or Unfading Bloom Co.):** \"Fading\" can sound negative, but can also evoke a gentle, soft beauty. \"Unfading\" is more positive.\n",
       "13. **Dusty Rose & Thyme:** Evokes specific dried flower colors/textures and a vintage feel.\n",
       "14. **The Gathered & Dried:** Simple, artisanal, and authentic.\n",
       "15. **Memory Petals:** Connects to sentiment and keepsakes.\n",
       "\n",
       "**III. Modern & Minimalist:**\n",
       "Clean, contemporary, and often one or two words.\n",
       "\n",
       "16. **Dry Bloom Co.** / **Drybloom:** Direct and trendy.\n",
       "17. **Everlast Florals:** Short, punchy, and clear.\n",
       "18. **The Preserve Co.:** Implies preservation and curation.\n",
       "19. **Still Bloom:** Evokes quiet beauty and permanence.\n",
       "20. **Petal.Dry:** Modern, almost like a domain name.\n",
       "21. **Airloom Florals:** A play on \"air-dried\" and \"heirloom.\"\n",
       "\n",
       "**IV. Direct & Descriptive:**\n",
       "These names clearly state what you offer, leaving no room for doubt.\n",
       "\n",
       "22. **The Dried Flower Bouquet Shop:** Very clear, though a bit long.\n",
       "23. **Eternal Bouquets:** Focuses on the product itself.\n",
       "24. **Preserved Flower Arrangements:** Professional and descriptive.\n",
       "25. **The Dried Petal Emporium:** Adds a touch of grandness to the directness.\n",
       "\n",
       "**Tips for Choosing:**\n",
       "\n",
       "*   **Say it out loud:** Does it roll off the tongue?\n",
       "*   **Check availability:** Is the name available as a domain name, social media handle, and business registration?\n",
       "*   **Consider your target audience:** Are they more traditional, modern, eco-conscious?\n",
       "*   **Reflect your brand personality:** Do you want to be quirky, sophisticated, rustic, or modern?\n",
       "*   **Get feedback:** Ask friends, family, and potential customers what they think.\n",
       "\n",
       "Good luck with your unique flower shop!"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"What do you think could be a good name for a flower shop that specializes in selling bouquets of dried flowers more than fresh flowers?\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "YrJexRHJYnmC"
   },
   "source": [
    "✅ Recommended. The prompt below is to the point and concise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "VHetn9lCYrXB"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "Here are some name suggestions for a flower shop specializing in dried flower bouquets, categorized by their style:\n",
       "\n",
       "**Evocative & Poetic:**\n",
       "\n",
       "1.  **Whispering Petals:** Evokes a gentle, timeless beauty.\n",
       "2.  **Echoing Blooms:** Suggests lasting beauty and memories.\n",
       "3.  **Everbloom & Co.** (or Everbloom Botanicals): Simple, direct, and elegant.\n",
       "4.  **The Memory Bloom:** Focuses on the keepsake aspect.\n",
       "5.  **Faded Grace:** Highlights the preserved beauty and rustic charm.\n",
       "6.  **Still Life Florals:** Connects to art and enduring beauty.\n",
       "7.  **Poetic Posies:** Alliterative and charming.\n",
       "8.  **Petal Perpetual:** Suggests unending beauty.\n",
       "\n",
       "**Rustic & Earthy:**\n",
       "\n",
       "9.  **The Dried Garden:** Simple and descriptive.\n",
       "10. **Root & Bloom Preserved:** Connects to the earth and the process.\n",
       "11. **Harvest & Bloom:** Implies natural gathering and enduring beauty.\n",
       "12. **Wild Bloom Collective:** Suggests natural, foraged aesthetics.\n",
       "13. **Earth & Stem:** Down-to-earth and natural.\n",
       "14. **Sylvan Blooms:** (Sylvan refers to woods/forests) – rustic, natural feel.\n",
       "\n",
       "**Charming & Whimsical:**\n",
       "\n",
       "15. **The Gentle Posy:** Soft, inviting, and classic.\n",
       "16. **Bloom & Press:** Hints at the preservation method.\n",
       "17. **Sun-Kissed Stems:** Implies a natural drying process and warmth.\n",
       "18. **The Little Dried Shop:** Quaint and memorable.\n",
       "19. **Flora & Fawn:** Evokes a gentle, woodland charm.\n",
       "\n",
       "**Modern & Elegant:**\n",
       "\n",
       "20. **Botanical Endearments:** Sophisticated and sentimental.\n",
       "21. **The Preservatory:** A unique twist on \"conservatory\" for preserved items.\n",
       "22. **Heirloom Botanicals:** Suggests cherished, long-lasting pieces.\n",
       "23. **Curated Petals:** Implies a carefully selected, high-quality collection.\n",
       "24. **FlorEver:** A blend of \"floral\" and \"forever.\"\n",
       "25. **Aeterna Flora:** (Latin for \"eternal flowers\") – refined and classic.\n",
       "\n",
       "**Tips for Choosing:**\n",
       "\n",
       "*   **Say it out loud:** Does it roll off the tongue?\n",
       "*   **Check availability:** Is the name available as a domain name, social media handle, and business registration?\n",
       "*   **Consider your target audience:** Does the name appeal to them?\n",
       "*   **Reflect your brand:** Does it match the overall aesthetic and feeling you want for your shop?\n",
       "*   **Keep it memorable:** Easy to remember and spell.\n",
       "\n",
       "Good luck with your new venture!"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"Suggest a name for a flower shop that sells bouquets of dried flowers\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "eXTAvdOHY0OC"
   },
   "source": [
    "### Be specific, and well-defined"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "FTH4GEIgY1dp"
   },
   "source": [
    "Suppose that you want to brainstorm creative ways to describe Earth."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "o5BmXBiGY4KC"
   },
   "source": [
    "🛑 The prompt below might be a bit too generic (which is certainly OK if you'd like to ask a generic question!)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "id": "eHBaMvv7Y6mR"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "Earth is a truly extraordinary and unique planet, often referred to as the \"Blue Marble\" due to its abundant water. Here's a comprehensive look at our home:\n",
       "\n",
       "### 1. Basic Identity & Location\n",
       "\n",
       "*   **Third planet from the Sun:** Earth is positioned in the \"Goldilocks Zone\" – not too hot, not too cold – allowing for liquid water.\n",
       "*   **Terrestrial Planet:** It's a rocky planet, unlike the gas giants further out in our solar system.\n",
       "*   **Only known celestial body to harbor life:** This is its most distinguishing feature.\n",
       "*   **Name Origin:** \"Earth\" is derived from both English and German words, \"eorðe\" and \"erde\" respectively, meaning \"ground.\"\n",
       "\n",
       "### 2. Physical Characteristics\n",
       "\n",
       "*   **Size:** It's the fifth largest planet in our solar system by diameter and mass.\n",
       "*   **Shape:** Not a perfect sphere, but an **oblate spheroid**. It bulges slightly at the equator due to its rotation and is flattened at the poles.\n",
       "*   **Diameter:** Approximately 12,756 km (7,926 miles) at the equator.\n",
       "*   **Mass:** Roughly 5.97 x 10^24 kg.\n",
       "*   **Surface Gravity:** 9.8 m/s² (1 G).\n",
       "\n",
       "### 3. Internal Structure\n",
       "\n",
       "Earth is composed of several distinct layers:\n",
       "\n",
       "*   **Crust:** The outermost solid layer, varying in thickness from about 5-70 km (3-43 miles). It's where we live and is divided into continental and oceanic crust.\n",
       "*   **Mantle:** A thick, semi-solid, rocky layer about 2,900 km (1,800 miles) thick, making up about 84% of Earth's volume. Convection currents in the mantle drive plate tectonics.\n",
       "*   **Outer Core:** A liquid layer, primarily composed of iron and nickel, about 2,200 km (1,400 miles) thick. Its movement generates Earth's magnetic field.\n",
       "*   **Inner Core:** A solid ball of iron and nickel, about 1,220 km (760 miles) in radius. It's incredibly hot (similar to the Sun's surface) and under immense pressure.\n",
       "\n",
       "### 4. Atmosphere\n",
       "\n",
       "Earth's atmosphere is a crucial blanket of gases that makes life possible:\n",
       "\n",
       "*   **Composition:** Approximately 78% Nitrogen, 21% Oxygen, 0.9% Argon, 0.04% Carbon Dioxide, and trace amounts of other gases.\n",
       "*   **Functions:**\n",
       "    *   Provides breathable air.\n",
       "    *   Traps heat (greenhouse effect), regulating temperature.\n",
       "    *   Protects from harmful solar radiation (ozone layer in the stratosphere).\n",
       "    *   Burns up most incoming meteors.\n",
       "*   **Layers:** Troposphere, Stratosphere, Mesosphere, Thermosphere, Exosphere.\n",
       "\n",
       "### 5. Hydrosphere (Water)\n",
       "\n",
       "Earth is truly the \"water planet\":\n",
       "\n",
       "*   **Coverage:** About 71% of Earth's surface is covered by water.\n",
       "*   **Distribution:**\n",
       "    *   **97% Salty Water:** Found in oceans.\n",
       "    *   **3% Freshwater:** Most of this is locked in glaciers and ice caps (68%), followed by groundwater (30%), with only a tiny fraction in rivers, lakes, and the atmosphere.\n",
       "*   **Water Cycle:** A continuous process of evaporation, condensation, precipitation, and runoff, vital for distributing water around the globe.\n",
       "\n",
       "### 6. Biosphere (Life)\n",
       "\n",
       "*   **Biodiversity:** Earth boasts an incredible diversity of life forms, from microscopic bacteria to gigantic whales, adapted to nearly every environment imaginable.\n",
       "*   **Ecosystems:** Life thrives in complex, interconnected ecosystems across land, air, and sea.\n",
       "*   **Key Factors for Life:** Liquid water, a stable temperature range, a protective atmosphere, and a consistent energy source (the Sun).\n",
       "\n",
       "### 7. Plate Tectonics\n",
       "\n",
       "*   **Dynamic Surface:** Earth's crust is broken into several large and small **tectonic plates** that are constantly moving, albeit slowly.\n",
       "*   **Geological Activity:** This movement causes earthquakes, volcanic eruptions, the formation of mountain ranges, and deep ocean trenches. It also recycles the Earth's crust over geological timescales.\n",
       "\n",
       "### 8. Earth's Moon\n",
       "\n",
       "*   **Single Natural Satellite:** Earth has one large moon, which is the fifth largest moon in the solar system.\n",
       "*   **Influence:**\n",
       "    *   **Tides:** Its gravitational pull is the primary cause of ocean tides.\n",
       "    *   **Stabilizes Tilt:** It helps stabilize Earth's axial tilt, which in turn contributes to Earth's relatively stable climate over long periods.\n",
       "\n",
       "### 9. Rotation & Orbit\n",
       "\n",
       "*   **Rotation:** Completes one rotation on its axis approximately every 24 hours (creating day and night).\n",
       "*   **Orbit:** Orbits the Sun in approximately 365.25 days (defining a year).\n",
       "*   **Axial Tilt:** Earth's axis is tilted about 23.5 degrees relative to its orbit, which is responsible for the changing seasons.\n",
       "\n",
       "### 10. Magnetic Field (Magnetosphere)\n",
       "\n",
       "*   **Origin:** Generated by the convection currents of molten iron in the outer core (the \"geodynamo\").\n",
       "*   **Protection:** It creates a protective shield called the magnetosphere that deflects harmful charged particles from the solar wind and cosmic rays, preventing them from stripping away our atmosphere.\n",
       "*   **Auroras:** When some charged particles penetrate the field near the poles, they interact with atmospheric gases, creating the beautiful auroras (Northern and Southern Lights).\n",
       "\n",
       "### 11. Humanity & The Future\n",
       "\n",
       "*   **Human Impact:** As the dominant species, humanity has a profound impact on Earth's systems, including climate, biodiversity, and natural resources.\n",
       "*   **Conservation:** Understanding and protecting Earth's delicate balance is crucial for the future of all life, including our own.\n",
       "*   **Ongoing Exploration:** Scientists continue to study Earth's complex systems, from its deep interior to the furthest reaches of its atmosphere, to better understand our planet and how it functions.\n",
       "\n",
       "Earth is a marvel of planetary science, a dynamic and interconnected system that continues to surprise and inspire us. It is our home, and its preservation is our shared responsibility."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"Tell me about Earth\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "4iyvEbteZnFL"
   },
   "source": [
    "✅ Recommended. The prompt below is specific and well-defined."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "id": "JQ80z8urZnne"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "Earth is a truly remarkable planet, often described as a \"Goldilocks\" world because so many factors aligned perfectly for it to host and sustain life as we know it. Here are several ways Earth stands out compared to other planets we know:\n",
       "\n",
       "1.  **Abundant Surface Liquid Water:** While other celestial bodies have ice or atmospheric water vapor, Earth is the only known planet to have vast oceans and significant amounts of *liquid water on its surface* for extended periods. This is fundamental for life.\n",
       "\n",
       "2.  **Oxygen-Rich Atmosphere (Biogenic):** Earth's atmosphere is unique with about 21% free oxygen, which is essential for complex aerobic life. This oxygen is not primordial; it was largely *produced by life itself* (photosynthesis) over billions of years, making it a biological signature. Other planets have atmospheres dominated by carbon dioxide, hydrogen, helium, or are extremely thin.\n",
       "\n",
       "3.  **Plate Tectonics:** Earth is the only planet in our solar system confirmed to have active, large-scale plate tectonics. This process constantly recycles the planet's crust, leading to continental drift, mountain building, volcanism, and earthquakes. This geological activity plays a crucial role in regulating Earth's climate (e.g., through the carbon cycle) and creating diverse habitats.\n",
       "\n",
       "4.  **Powerful Global Magnetic Field (Magnetosphere):** Generated by Earth's molten iron core, this magnetic field creates a protective shield that deflects harmful solar wind and cosmic rays. This prevents the solar wind from stripping away our atmosphere and makes the surface safe for life. Other rocky planets either lack a significant global field (Mars, Venus) or have only remnant, localized fields.\n",
       "\n",
       "5.  **Large, Stabilizing Moon:** Earth has an unusually large moon relative to its size, which was likely formed from a giant impact. This large moon exerts strong tidal forces, which may have helped kick-start plate tectonics. More importantly, it acts as a gravitational anchor, *stabilizing Earth's axial tilt*. This stability prevents drastic, chaotic shifts in tilt that would lead to extreme climate fluctuations, ensuring long-term climate stability.\n",
       "\n",
       "6.  **Biodiversity and Complex Life:** While the existence of microbial life elsewhere is highly anticipated, Earth is the only known planet teeming with an astounding diversity of complex, multicellular life, including plants, animals, fungi, and ultimately, intelligent life.\n",
       "\n",
       "7.  **Intelligent, Technologically Advanced Civilization:** To our current knowledge, Earth is the only planet where intelligent life has evolved to the point of developing technology, science, art, and the ability to explore space.\n",
       "\n",
       "8.  **Habitable Zone Sweet Spot (\"Goldilocks Zone\"):** Earth orbits the Sun at just the right distance where temperatures allow liquid water to exist on its surface. It's not too hot (like Venus) and not too cold (like Mars or beyond). This, combined with its atmospheric composition, allows for a relatively stable and temperate climate.\n",
       "\n",
       "9.  **Hydrological Cycle:** The continuous movement of water between the oceans, atmosphere, and land (evaporation, condensation, precipitation) is a defining feature of Earth. This cycle is driven by the sun's energy and gravity and is vital for weather patterns, climate regulation, and sustaining ecosystems.\n",
       "\n",
       "10. **Complex Interacting Systems (Geosphere, Hydrosphere, Atmosphere, Biosphere):** Earth is characterized by a dynamic and intricate interplay between its various spheres. Life (biosphere) profoundly impacts the atmosphere, oceans, and geology, and vice-versa, creating a self-regulating system that maintains conditions favorable for life over geological timescales.\n",
       "\n",
       "These unique characteristics highlight Earth's exceptional nature in the cosmos we currently observe."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"Generate a list of ways that makes Earth unique compared to other planets\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "R5kmfZYHZsJ7"
   },
   "source": [
    "### Ask one task at a time"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "rsAezxeYZuUN"
   },
   "source": [
    "🛑 Not recommended. The prompt below has two parts to the question that could be asked separately."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "ElywPXpuZtWf"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "Let's break down both of those fascinating questions!\n",
       "\n",
       "---\n",
       "\n",
       "### What's the best method of boiling water?\n",
       "\n",
       "\"Best\" can depend on your priorities (speed, energy efficiency, volume, convenience, portability), but generally, for most home uses, the top contenders are:\n",
       "\n",
       "1.  **Electric Kettle:**\n",
       "    *   **Why it's often the best:** For typical household quantities (1-2 liters), an electric kettle is usually the **fastest and most energy-efficient** method. It heats the water directly with an immersed heating element, and modern kettles often have good insulation and automatic shut-off features, preventing over-boiling and wasted energy.\n",
       "    *   **Pros:** Very fast, energy-efficient, safe (auto-shutoff), convenient, portable (within range of an outlet).\n",
       "    *   **Cons:** Limited capacity, requires electricity.\n",
       "\n",
       "2.  **Induction Stovetop (with an induction-compatible pot):**\n",
       "    *   **Why it's excellent:** Induction stovetops create a magnetic field that directly heats the cookware itself, which in turn heats the water. This is incredibly efficient, as very little heat is lost to the surrounding air. It's often **comparable in speed to an electric kettle** for similar volumes and superior for larger volumes.\n",
       "    *   **Pros:** Very fast, highly energy-efficient, precise temperature control, good for any volume (limited only by pot size).\n",
       "    *   **Cons:** Requires induction-compatible pots/pans, stovetops themselves can be expensive.\n",
       "\n",
       "3.  **Gas Stovetop:**\n",
       "    *   **Why it's good:** Gas stoves provide a powerful, immediate flame. While not quite as energy-efficient as an electric kettle or induction (because some heat escapes around the pot), they are still **very fast and powerful**, especially for larger pots.\n",
       "    *   **Pros:** Fast, good for large volumes, precise control over heat, works during power outages.\n",
       "    *   **Cons:** Less energy-efficient than induction/electric kettle (heat loss), open flame safety concerns.\n",
       "\n",
       "**Methods generally NOT considered \"best\" for efficiency or speed:**\n",
       "\n",
       "*   **Electric Coil/Radiant Stovetop:** These are generally slower and less energy-efficient as they have to heat up the entire burner first, and then transfer that heat to the pot.\n",
       "*   **Microwave:** While convenient for a single cup of water, microwaves are **not energy-efficient** for boiling water, heat unevenly, and carry a slight risk of superheating (where the water boils suddenly and explosively when disturbed).\n",
       "\n",
       "**General tip for any method:** Always use a **lid** on your pot or kettle. This significantly reduces heat loss and speeds up the boiling process, saving energy.\n",
       "\n",
       "---\n",
       "\n",
       "### Why is the sky blue?\n",
       "\n",
       "The blue color of the sky is due to a phenomenon called **Rayleigh Scattering**. Here's how it works:\n",
       "\n",
       "1.  **Sunlight is White Light:** Sunlight, which appears white to our eyes, is actually made up of all the colors of the rainbow, each with a different wavelength. Violet and blue light have shorter wavelengths, while red and orange light have longer wavelengths.\n",
       "\n",
       "2.  **Earth's Atmosphere:** The Earth's atmosphere is composed of tiny gas molecules, primarily nitrogen (about 78%) and oxygen (about 21%). These molecules are much smaller than the wavelengths of visible light.\n",
       "\n",
       "3.  **Rayleigh Scattering:** When sunlight enters the Earth's atmosphere, these tiny gas molecules scatter the light. However, they don't scatter all colors equally. According to Rayleigh Scattering, **shorter wavelengths of light (like blue and violet) are scattered much more effectively and in all directions than longer wavelengths (like red and yellow).**\n",
       "\n",
       "4.  **Blue Light Dominates:** Because blue light is scattered far more efficiently than other colors, it appears to come from all directions in the sky. When you look up, you see this scattered blue light, making the sky appear blue. Violet light is scattered even more, but our eyes are less sensitive to violet, and there's less violet in the sun's spectrum to begin with, so blue predominates.\n",
       "\n",
       "5.  **What Happens to Other Colors?** The longer wavelengths (red, orange, yellow) are scattered much less by the atmosphere's molecules. They tend to pass straight through the atmosphere to our eyes, which is why the sun itself appears yellowish-white when high in the sky (the blue light has been scattered away).\n",
       "\n",
       "**Why Sunrises and Sunsets are Red/Orange:**\n",
       "\n",
       "When the sun is low on the horizon (at sunrise or sunset), its light has to travel through a much greater amount of the Earth's atmosphere to reach our eyes. During this longer journey, even more blue and green light gets scattered away. What's left are primarily the longer wavelengths – red, orange, and some yellow – which we then see, creating those beautiful, warm colors in the sky. Dust and pollution in the atmosphere can also enhance this effect by scattering more of the blue light away.\n",
       "\n",
       "**Why Space is Black:**\n",
       "\n",
       "In space, there is no atmosphere (or very few particles), so there are no molecules to scatter the sunlight. Therefore, there is no scattered light to reach our eyes, and the sky appears black."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"What's the best method of boiling water and why is the sky blue?\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ejzahazBZ8vk"
   },
   "source": [
    "✅ Recommended. The prompts below asks one task a time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "id": "C5ckp2F0Z_Ba"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "The \"best\" method for boiling water really depends on your priorities: **speed, energy efficiency, convenience, cost, and access to utilities.**\n",
       "\n",
       "Here's a breakdown of common methods and their pros and cons:\n",
       "\n",
       "---\n",
       "\n",
       "### 1. Electric Kettle (Overall Best for Most People)\n",
       "\n",
       "*   **Pros:**\n",
       "    *   **Fastest:** Typically boils water quicker than a stovetop.\n",
       "    *   **Energy Efficient:** Heats only the water directly, with minimal heat loss. Many models have automatic shut-off, preventing wasted energy once boiling.\n",
       "    *   **Convenient:** Cordless design, easy to fill and pour, requires only an electrical outlet.\n",
       "    *   **Safe:** Auto shut-off prevents dry boiling and overheating.\n",
       "*   **Cons:**\n",
       "    *   Initial purchase cost.\n",
       "    *   Takes up counter space.\n",
       "    *   Requires electricity.\n",
       "*   **Best for:** Everyday use, tea, coffee, instant noodles, generally anyone with access to electricity who wants fast, efficient boiling.\n",
       "\n",
       "---\n",
       "\n",
       "### 2. Induction Stovetop (Potentially Fastest & Most Efficient with Right Gear)\n",
       "\n",
       "*   **Pros:**\n",
       "    *   **Extremely Fast:** Often as fast, or even faster, than an electric kettle, especially with a good induction-compatible pot.\n",
       "    *   **Highly Energy Efficient:** Directly heats the magnetic cookware, with very little heat loss to the surrounding air.\n",
       "    *   **Precise Control:** Allows for very fine temperature adjustments.\n",
       "    *   **Safe:** The cooktop itself doesn't get hot (only the pot does), reducing burn risk.\n",
       "*   **Cons:**\n",
       "    *   Requires induction-compatible cookware (magnetic bottom).\n",
       "    *   Higher initial cost for the induction cooktop itself.\n",
       "    *   Requires electricity.\n",
       "*   **Best for:** Those with an induction stovetop and appropriate cookware who prioritize speed and efficiency.\n",
       "\n",
       "---\n",
       "\n",
       "### 3. Gas Stovetop (Traditional & Versatile)\n",
       "\n",
       "*   **Pros:**\n",
       "    *   **Versatile:** Can use any type of pot or kettle.\n",
       "    *   **Relatively Fast:** Faster than electric coil stovetops, but generally slower than electric kettles or induction.\n",
       "    *   **Reliable:** Works during power outages (can be lit with a match if pilot light is out).\n",
       "*   **Cons:**\n",
       "    *   **Less Energy Efficient:** A lot of heat escapes around the pot into the air.\n",
       "    *   Requires constant supervision.\n",
       "    *   Open flame presents a safety hazard.\n",
       "*   **Best for:** Boiling large quantities of water, cooking purposes, or when electricity isn't available.\n",
       "\n",
       "---\n",
       "\n",
       "### 4. Electric Coil/Radiant Stovetop (Slower & Less Efficient)\n",
       "\n",
       "*   **Pros:**\n",
       "    *   **Common:** Found in many kitchens.\n",
       "    *   **Versatile:** Can use any type of pot.\n",
       "*   **Cons:**\n",
       "    *   **Slowest** of the stovetop methods.\n",
       "    *   **Least Energy Efficient:** The burner itself heats up, then transfers heat to the pot, leading to significant heat loss.\n",
       "    *   Requires constant supervision.\n",
       "    *   Burners remain hot for a long time after turning off.\n",
       "*   **Best for:** When it's the only option available.\n",
       "\n",
       "---\n",
       "\n",
       "### 5. Microwave (Not Recommended for Boiling, but possible for small amounts)\n",
       "\n",
       "*   **Pros:**\n",
       "    *   **Convenient for very small amounts:** Quick for a single cup if you don't have an alternative.\n",
       "    *   No specialized equipment beyond a microwave-safe cup.\n",
       "*   **Cons:**\n",
       "    *   **Slow for boiling:** Not efficient for larger volumes.\n",
       "    *   **Uneven Heating:** Can lead to \"superheating\" (water heats above boiling point without bubbling), which can cause explosive boiling when disturbed. This is a significant safety risk.\n",
       "    *   No visible indicator of boiling.\n",
       "*   **Best for:** *Only* when you need a very small amount of hot water in a pinch and have no other option. **Use extreme caution (put a non-metallic stir stick in the cup).**\n",
       "\n",
       "---\n",
       "\n",
       "### 6. Campfire / Open Flame (Off-Grid)\n",
       "\n",
       "*   **Pros:**\n",
       "    *   Works without electricity or gas.\n",
       "    *   Useful for camping, survival, or off-grid living.\n",
       "*   **Cons:**\n",
       "    *   Slow and inefficient.\n",
       "    *   Requires fuel and fire management.\n",
       "    *   Smoky, dirty.\n",
       "*   **Best for:** Outdoor cooking, survival situations.\n",
       "\n",
       "---\n",
       "\n",
       "### Tips for Efficient and Safe Boiling (Regardless of Method):\n",
       "\n",
       "1.  **Use a Lid:** Always put a lid on your pot or kettle. This traps heat, brings water to a boil much faster, and saves energy.\n",
       "2.  **Only Boil What You Need:** Don't fill a 2-liter kettle for one cup of tea. This saves time and energy.\n",
       "3.  **Use the Right Pot Size:** A pot that's too large for the amount of water will take longer to heat up the pot itself.\n",
       "4.  **Clean Your Kettle/Pot:** Limescale buildup in electric kettles can reduce efficiency.\n",
       "5.  **Safety First:** Never leave boiling water unattended, especially on a stovetop. Be aware of steam burns.\n",
       "6.  **Altitude Matters:** At higher altitudes, water boils at a lower temperature, and it can take longer to reach that boiling point.\n",
       "\n",
       "---\n",
       "\n",
       "### Conclusion:\n",
       "\n",
       "For most modern households, an **electric kettle** is the \"best\" all-around method due to its speed, energy efficiency, and convenience. If you have an **induction stovetop** and compatible cookware, that's often an even faster and more efficient choice."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"What's the best method of boiling water?\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "KwUzhud4aA89"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "The sky is blue because of a phenomenon called **Rayleigh scattering**. Here's a breakdown of how it works:\n",
       "\n",
       "1.  **Sunlight is White Light:** Sunlight, which appears white to us, is actually made up of all the colors of the visible spectrum (red, orange, yellow, green, blue, indigo, violet). Each color has a different **wavelength** – red light has the longest wavelength, and violet/blue light has the shortest.\n",
       "\n",
       "2.  **Earth's Atmosphere:** Our atmosphere is composed mainly of tiny gas molecules, primarily nitrogen (N2) and oxygen (O2). These molecules are much smaller than the wavelengths of visible light.\n",
       "\n",
       "3.  **Rayleigh Scattering:** When sunlight enters the Earth's atmosphere, it interacts with these tiny gas molecules. Rayleigh scattering states that:\n",
       "    *   **Shorter wavelengths of light (like blue and violet) are scattered much more effectively than longer wavelengths (like red, orange, and yellow).** Think of it like ocean waves hitting a small rock: short, choppy waves get bounced around easily in all directions, while long, sweeping waves tend to pass by relatively undisturbed.\n",
       "    *   Blue light is scattered about 10 times more than red light.\n",
       "\n",
       "4.  **Why We See Blue:**\n",
       "    *   As sunlight travels through the atmosphere, the blue and violet components are scattered in all directions by the gas molecules.\n",
       "    *   When we look up at the sky, we are seeing this scattered blue light coming from all directions above us.\n",
       "\n",
       "5.  **Why Blue and Not Violet?**\n",
       "    *   Violet light is scattered even more than blue light, so theoretically, the sky should appear violet. However, there are two main reasons it looks blue:\n",
       "        1.  **The Sun's Spectrum:** The sun actually emits slightly less violet light than blue light.\n",
       "        2.  **Our Eyes' Sensitivity:** Human eyes are more sensitive to blue light than to violet light. Our cones (color receptors) respond more strongly to blue. The combination of some scattered violet light and a lot of scattered blue light, along with our eye's sensitivity, results in us perceiving the sky as blue.\n",
       "\n",
       "6.  **What Happens to Other Colors?**\n",
       "    *   The longer wavelengths (red, orange, yellow) are not scattered as much. They tend to pass straight through the atmosphere to our eyes, which is why the sun usually appears yellowish-white when it's high in the sky.\n",
       "\n",
       "This scattering effect is also why sunrises and sunsets often appear red or orange. When the sun is low on the horizon, its light has to travel through a much thicker layer of atmosphere. By the time it reaches your eyes, most of the blue and violet light has been scattered away, leaving primarily the longer-wavelength red and orange light to be seen directly."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"Why is the sky blue?\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "PJIL2RTQaGcT"
   },
   "source": [
    "### Watch out for hallucinations"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "8Y8kYxrSaHE9"
   },
   "source": [
    "Although LLMs have been trained on a large amount of data, they can generate text containing statements not grounded in truth or reality; these responses from the LLM are often referred to as \"hallucinations\" due to their limited memorization capabilities. Note that simply prompting the LLM to provide a citation isn't a fix to this problem, as there are instances of LLMs providing false or inaccurate citations. Dealing with hallucinations is a fundamental challenge of LLMs and an ongoing research area, so it is important to be cognizant that LLMs may seem to give you confident, correct-sounding statements that are in fact incorrect.\n",
    "\n",
    "Note that if you intend to use LLMs for the creative use cases, hallucinating could actually be quite useful."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "8NY5nAGeaJYS"
   },
   "source": [
    "Try the prompt like the one below repeatedly. We set the temperature to `1.0` so that it takes more risks in its choices. It's possible that it may provide an inaccurate, but confident answer."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "id": "QALPjEILaM62"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "I don't have a real-time clock, so I don't know what today's date is for you right now.\n",
       "\n",
       "You can easily check your device's clock or calendar!"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "generation_config = GenerateContentConfig(temperature=1.0)\n",
    "\n",
    "prompt = \"What day is it today?\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "BRkwzbgRbhKt"
   },
   "source": [
    "Since LLMs do not have access to real-time information without further integrations, you may have noticed it hallucinates what day it is today in some of the outputs."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "3c811e310d02"
   },
   "source": [
    "### Using system instructions to guardrail the model from irrelevant responses\n",
    "\n",
    "How can we attempt to reduce the chances of irrelevant responses and hallucinations?\n",
    "\n",
    "One way is to provide the LLM with [system instructions](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instruction-introduction).\n",
    "\n",
    "Let's see how system instructions works and how you can use them to reduce hallucinations or irrelevant questions for a travel chatbot.\n",
    "\n",
    "Suppose we ask a simple question about one of Italy's most famous tourist spots."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "rB6zJU76biFK"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "Milan offers a fantastic array of sights! Here are some of the top places for sightseeing in Milan:\n",
       "\n",
       "1.  **Duomo di Milano (Milan Cathedral):** This is undeniably the most iconic landmark. Its Gothic architecture is breathtaking, and you can climb to the terraces for incredible panoramic views of the city.\n",
       "2.  **Galleria Vittorio Emanuele II:** An exquisite 19th-century shopping arcade, often called \"Milan's drawing room.\" Even if you're not shopping, it's stunning to walk through, admire the architecture, mosaics, and dome.\n",
       "3.  **Sforza Castle (Castello Sforzesco):** A massive medieval fortress that now houses several museums and art collections, including Michelangelo's last sculpture, the Rondanini Pietà. It's surrounded by the beautiful Parco Sempione.\n",
       "4.  **Santa Maria delle Grazie:** This church is home to Leonardo da Vinci's masterpiece, \"The Last Supper.\" Booking tickets far in advance is essential due to high demand.\n",
       "5.  **Teatro alla Scala:** One of the world's most famous opera houses. You can take a guided tour to see the interior and visit its museum, even if you don't attend a performance.\n",
       "6.  **Brera District and Pinacoteca di Brera:** The Brera district is charming with its narrow cobbled streets, boutiques, and cafes. The Pinacoteca di Brera is an important art gallery housing masterpieces by Italian artists.\n",
       "\n",
       "For a comprehensive sightseeing experience, I'd recommend starting with the Duomo, Galleria Vittorio Emanuele II, and Sforza Castle, as they are relatively close to each other in the city center. Enjoy your trip to Milan!"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "generation_config = GenerateContentConfig(temperature=1.0)\n",
    "\n",
    "chat = client.chats.create(\n",
    "    model=MODEL_ID,\n",
    "    config=GenerateContentConfig(\n",
    "        system_instruction=[\n",
    "            \"Hello! You are an AI chatbot for a travel web site.\",\n",
    "            \"Your mission is to provide helpful queries for travelers.\",\n",
    "            \"Remember that before you answer a question, you must check to see if it complies with your mission.\",\n",
    "            \"If not, you can say, Sorry I can't answer that question.\",\n",
    "        ]\n",
    "    ),\n",
    ")\n",
    "\n",
    "prompt = \"What is the best place for sightseeing in Milan, Italy?\"\n",
    "\n",
    "response = chat.send_message(prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "WZa-Qcf9cF4A"
   },
   "source": [
    "Now let us pretend to be a user asks the chatbot a question that is unrelated to travel."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "id": "AZKBIDr2cGnu"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "Sorry, I can't answer that question."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"How do I make pizza dough at home?\"\n",
    "\n",
    "response = chat.send_message(prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JiUYIhwpctCy"
   },
   "source": [
    "You can see that this way, a guardrail in the prompt prevented the chatbot from veering off course."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ZuuDhA37cvmP"
   },
   "source": [
    "### Turn generative tasks into classification tasks to reduce output variability"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "kUCUrsUzczmb"
   },
   "source": [
    "#### Generative tasks lead to higher output variability"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "a1xASHAkc46n"
   },
   "source": [
    "The prompt below results in an open-ended response, useful for brainstorming, but response is highly variable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "id": "nPfXQWIacwRf"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "That's fantastic! Deciding to actively improve your programming skills in high school puts you in a great position. The best activity depends on your current skill level, interests, and how you like to learn.\n",
       "\n",
       "Here are several recommendations, ranging from structured problem-solving to creative project building:\n",
       "\n",
       "---\n",
       "\n",
       "### **1. Build a Personal Project (Highly Recommended for High Schoolers!)**\n",
       "\n",
       "This is arguably the most impactful way to learn and demonstrate your skills. It allows you to apply theoretical knowledge to a real-world (or fun-world) problem.\n",
       "\n",
       "**Why it's great:**\n",
       "*   **Motivation:** You're building something *you* care about.\n",
       "*   **Full Stack Learning:** You'll encounter front-end, back-end, database, deployment, and problem-solving.\n",
       "*   **Portfolio Piece:** You'll have something tangible to show off.\n",
       "*   **Debugging Skills:** You'll learn how to find and fix your own errors.\n",
       "\n",
       "**Ideas (start small!):**\n",
       "\n",
       "*   **Personal Website/Portfolio:**\n",
       "    *   **Skills:** HTML, CSS, JavaScript (JS). Later: Frameworks like React/Vue.\n",
       "    *   **Why:** Learn web fundamentals, design, responsiveness. Essential for showing off other projects.\n",
       "*   **Simple Game:**\n",
       "    *   **Skills:** Python (Pygame), JavaScript (browser games), C# (Unity, if you're ambitious).\n",
       "    *   **Why:** Logic, game loops, user input, graphics.\n",
       "    *   **Examples:** Tic-Tac-Toe, Hangman, Snake, a simple platformer, a text-based adventure game.\n",
       "*   **To-Do List/Task Manager App:**\n",
       "    *   **Skills:** Web (HTML/CSS/JS with local storage or a simple backend like Flask/Node.js), or desktop (Python with Tkinter/PyQt).\n",
       "    *   **Why:** Data persistence, user interface design, basic CRUD (Create, Read, Update, Delete) operations.\n",
       "*   **Web Scraper/Automation Script:**\n",
       "    *   **Skills:** Python (BeautifulSoup, Requests, Selenium), Node.js.\n",
       "    *   **Why:** Interacting with web data, automating repetitive tasks (e.g., getting weather, stock prices, sports scores).\n",
       "    *   **Examples:** A script to automatically rename files, organize downloads, or send you daily jokes.\n",
       "*   **Simple Calculator:**\n",
       "    *   **Skills:** Any language. Focus on UI, arithmetic operations, error handling.\n",
       "*   **Discord Bot or Chatbot:**\n",
       "    *   **Skills:** Python (discord.py), Node.js.\n",
       "    *   **Why:** API interaction, event handling, community engagement.\n",
       "\n",
       "**How to get started:**\n",
       "1.  **Pick one project idea** that genuinely interests you.\n",
       "2.  **Choose a language** you're comfortable with or want to learn (Python and JavaScript are excellent for beginners).\n",
       "3.  **Break it down:** Don't try to build the whole thing at once. Start with the absolute core functionality, then add features.\n",
       "4.  **Google everything!** You'll constantly be looking up how to do things. That's normal.\n",
       "5.  **Use version control (Git/GitHub):** Learn the basics of `git commit`, `git push`. This is crucial for collaboration and tracking your work.\n",
       "\n",
       "---\n",
       "\n",
       "### **2. Competitive Programming / Coding Challenges**\n",
       "\n",
       "If you enjoy puzzles and want to sharpen your algorithmic thinking and problem-solving skills under timed pressure.\n",
       "\n",
       "**Why it's great:**\n",
       "*   **Problem-Solving:** Forces you to think logically and break down complex problems.\n",
       "*   **Algorithms & Data Structures:** You'll naturally learn and apply these essential concepts.\n",
       "*   **Efficiency:** You'll learn to write performant code.\n",
       "*   **Interview Prep:** Many tech company interviews use similar styles of problems.\n",
       "\n",
       "**Platforms:**\n",
       "*   **LeetCode:** Very popular, vast library of problems, great for interview prep.\n",
       "*   **HackerRank:** Good for beginners, offers tutorials and different domain challenges.\n",
       "*   **Codeforces:** More competitive, focuses on competitive programming style.\n",
       "*   **Advent of Code:** (Seasonal - December) A daily programming challenge with a fun storyline, great for holidays.\n",
       "*   **Project Euler:** Focuses on mathematical/computational problems.\n",
       "\n",
       "**How to get started:**\n",
       "1.  **Choose a platform.** LeetCode or HackerRank are good starting points.\n",
       "2.  **Start with \"Easy\" problems.** Don't jump into \"Hard\" ones immediately.\n",
       "3.  **Focus on understanding the solution:** Don't just copy-paste. Read other people's solutions after you've tried your best.\n",
       "4.  **Learn common algorithms and data structures:** Arrays, linked lists, trees, graphs, sorting, searching, recursion.\n",
       "\n",
       "---\n",
       "\n",
       "### **3. Contribute to Open Source (Beginner Friendly)**\n",
       "\n",
       "This might sound intimidating, but it's a fantastic way to learn about real-world codebases, collaboration, and Git.\n",
       "\n",
       "**Why it's great:**\n",
       "*   **Real-World Code:** You'll see how professional projects are structured.\n",
       "*   **Collaboration:** Learn how to work with others (pull requests, code reviews).\n",
       "*   **Git Proficiency:** Essential for any developer.\n",
       "*   **Community:** Become part of a larger developer community.\n",
       "\n",
       "**How to get started:**\n",
       "1.  **Look for projects with \"good first issue\" or \"beginner friendly\" labels on GitHub.**\n",
       "    *   Search GitHub for `is:issue is:open label:\"good first issue\" language:python` (replace `python` with your preferred language).\n",
       "2.  **Start small:** Fix a typo in documentation, improve a comment, add a small test case, or fix a minor bug.\n",
       "3.  **Read the contribution guidelines:** Most projects have a `CONTRIBUTING.md` file.\n",
       "4.  **Fork the repository, make your changes, and submit a pull request.**\n",
       "\n",
       "---\n",
       "\n",
       "### **4. Participate in a Hackathon**\n",
       "\n",
       "Intense, short-term events where teams build a project from scratch, often around a specific theme.\n",
       "\n",
       "**Why it's great:**\n",
       "*   **Rapid Learning:** You'll learn an incredible amount in a short time.\n",
       "*   **Teamwork & Communication:** Essential soft skills for developers.\n",
       "*   **Networking:** Meet other students and professionals.\n",
       "*   **Time Management:** Learn to work under pressure.\n",
       "*   **Fun & Energy:** The atmosphere is usually very exciting.\n",
       "\n",
       "**How to get started:**\n",
       "1.  **Look for high school specific hackathons** (e.g., local universities, organizations like Major League Hacking often list them).\n",
       "2.  **Go with friends or form a team there.** Don't worry if you're a beginner; many hackathons welcome and support new participants.\n",
       "3.  **Have a rough idea** of what you want to build or what skills you want to use.\n",
       "\n",
       "---\n",
       "\n",
       "### **5. Dive Deeper into a Specific Technology Stack**\n",
       "\n",
       "Once you have some basics, pick an area and go deep.\n",
       "\n",
       "*   **Front-End Web Development:** Master HTML, CSS, JavaScript, then move to a framework like React, Vue, or Angular. Build interactive UIs.\n",
       "*   **Back-End Web Development:** Learn Python (Flask/Django), Node.js (Express), or Ruby (Rails). Understand databases (SQL, NoSQL), APIs, and server logic.\n",
       "*   **Mobile App Development:** Learn Swift/Kotlin for native iOS/Android, or cross-platform tools like React Native or Flutter.\n",
       "*   **Data Science/Machine Learning:** Python with libraries like Pandas, NumPy, Scikit-learn. Start with simple data analysis, then move to basic ML models.\n",
       "\n",
       "---\n",
       "\n",
       "### **General Tips for Improvement:**\n",
       "\n",
       "*   **Consistency is Key:** Better to code for 30 minutes every day than 5 hours once a week.\n",
       "*   **Learn Git & GitHub:** This is non-negotiable for modern developers.\n",
       "*   **Read Code:** Look at how others solve problems. Read tutorials, open-source projects.\n",
       "*   **Explain Your Code:** Try to explain a concept or a piece of your code to someone else (or even a rubber duck!). This solidifies your understanding.\n",
       "*   **Don't Be Afraid to Debug:** Errors are your teachers. Learn how to read error messages and use a debugger.\n",
       "*   **Ask Questions:** Use platforms like Stack Overflow, Reddit communities (r/learnprogramming, r/Python, etc.), or Discord servers.\n",
       "*   **Have Fun!** If it feels like a chore, you're doing it wrong. Find aspects that genuinely excite you.\n",
       "\n",
       "---\n",
       "\n",
       "**Recommendation for a High Schooler starting out:**\n",
       "\n",
       "I'd suggest beginning with **Building a Personal Project** (like a simple personal website or a small game in Python/JS) combined with **Competitive Programming/Coding Challenges** on a platform like HackerRank or LeetCode (easy problems). This gives you both practical application and algorithmic skill development. And definitely get familiar with **Git/GitHub** early on!\n",
       "\n",
       "Good luck, and happy coding!"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"I'm a high school student. Recommend me a programming activity to improve my skills.\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "iAmm9wPYc_1o"
   },
   "source": [
    "#### Classification tasks reduces output variability"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "VvRpK_0GdCpf"
   },
   "source": [
    "The prompt below results in a choice and may be useful if you want the output to be easier to control."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "id": "kYDKh0r2dAqo"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "For a high school student, the choice of programming language can significantly impact your initial learning experience and what you can build. Let's break down each option:\n",
       "\n",
       "---\n",
       "\n",
       "### a) Learn Python\n",
       "\n",
       "**What it is:** A high-level, general-purpose programming language known for its readability and simplicity.\n",
       "**Commonly used for:**\n",
       "*   **Web Development (Backend):** Frameworks like Django and Flask.\n",
       "*   **Data Science & Machine Learning:** Libraries like NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch. This is a huge area.\n",
       "*   **Automation & Scripting:** Automating repetitive tasks, web scraping.\n",
       "*   **Game Development:** (e.g., Pygame)\n",
       "*   **Desktop Applications:** (though less common than web)\n",
       "*   **Education & Academia:** Widely used for teaching programming concepts.\n",
       "\n",
       "**Why I suggest it for a high school student:**\n",
       "\n",
       "*   **Extremely Beginner-Friendly:** Python's syntax is very clean and readable, often resembling plain English. This makes it much easier to grasp fundamental programming concepts without getting bogged down in complex syntax.\n",
       "*   **Versatility:** You can do almost anything with Python. This means your learning won't be limited to one specific area. You can explore data analysis, build simple games, create websites, or automate tasks.\n",
       "*   **Large & Supportive Community:** If you get stuck, there are countless tutorials, forums (like Stack Overflow), and online communities eager to help.\n",
       "*   **Rich Ecosystem of Libraries:** Python has an enormous collection of pre-written code (libraries) for almost any task, saving you time and effort.\n",
       "*   **High Demand in the Job Market:** While not your immediate concern, Python skills are highly sought after in many tech fields, especially data science and AI.\n",
       "*   **Great for Projects:** You can quickly build impressive projects that are both fun and useful, which is excellent for staying motivated.\n",
       "\n",
       "**When to choose Python:**\n",
       "*   You want the easiest entry into programming.\n",
       "*   You're interested in data science, artificial intelligence, scripting, or general-purpose programming.\n",
       "*   You want a language with broad applications.\n",
       "\n",
       "---\n",
       "\n",
       "### b) Learn JavaScript\n",
       "\n",
       "**What it is:** The programming language of the web. It's primarily used for making web pages interactive.\n",
       "**Commonly used for:**\n",
       "*   **Front-end Web Development:** Making websites dynamic, interactive, and responsive (what you see and click on).\n",
       "*   **Back-end Web Development:** With Node.js, JavaScript can also run on servers, creating full-stack applications.\n",
       "*   **Mobile App Development:** With frameworks like React Native.\n",
       "*   **Desktop App Development:** With frameworks like Electron.\n",
       "*   **Game Development:** In-browser games.\n",
       "\n",
       "**Why I suggest it for a high school student:**\n",
       "\n",
       "*   **Instant Visual Gratification:** You can immediately see the results of your code in a web browser. This can be incredibly motivating and fun as you build interactive elements, animations, or even simple games.\n",
       "*   **Highly Relevant to the Web:** If you use the internet, you're constantly interacting with JavaScript. Learning it gives you insight into how the web works and the power to build your own corner of it.\n",
       "*   **Full-Stack Potential:** If you eventually want to build complete web applications (both what the user sees and what happens behind the scenes), JavaScript (with Node.js) allows you to do it all with one language.\n",
       "*   **Massive Community & Resources:** Like Python, JavaScript has a huge and active community, with tons of tutorials, frameworks (React, Angular, Vue), and online courses.\n",
       "\n",
       "**When to choose JavaScript:**\n",
       "*   You're primarily interested in web development (making interactive websites).\n",
       "*   You want to see immediate visual results from your code.\n",
       "*   You're curious about how websites and web applications function.\n",
       "\n",
       "---\n",
       "\n",
       "### c) Learn Fortran\n",
       "\n",
       "**What it is:** One of the oldest programming languages, specifically designed for numerical computation and scientific computing.\n",
       "**Commonly used for:**\n",
       "*   **High-Performance Computing (HPC):** Supercomputers, scientific simulations.\n",
       "*   **Numerical Analysis:** Engineering, physics, chemistry, meteorology, aerospace.\n",
       "*   **Academic Research:** Many legacy scientific codes are written in Fortran.\n",
       "\n",
       "**Why I **do NOT** suggest it for a high school student (in most cases):**\n",
       "\n",
       "*   **Very Niche:** Fortran is highly specialized. Unless you have a very specific, pre-existing interest in high-performance scientific computing or numerical methods (which is rare for a general high school student), it won't be broadly useful.\n",
       "*   **Steeper Learning Curve for General Concepts:** Its syntax and paradigms are less intuitive and less \"general purpose\" than Python or JavaScript. It's not designed for building interactive applications or websites.\n",
       "*   **Less Immediate Fun/Visuals:** You won't be building websites, games, or user interfaces directly with Fortran. Your output will typically be numerical data or simulations, which might not be as engaging for a beginner.\n",
       "*   **Smaller Community & Fewer Beginner Resources:** While its community is dedicated, it's much smaller and more specialized than Python or JavaScript, and beginner-friendly resources are scarcer.\n",
       "*   **Limited General Applicability:** Learning Fortran won't easily transition into building mobile apps, web apps, or general automation tools, unlike Python or JavaScript.\n",
       "\n",
       "**When to choose Fortran:**\n",
       "*   **Only if:** You are *already* deeply passionate about high-performance scientific computing, numerical analysis, or engineering simulations, *and* you might be following a very specific academic path that requires it (e.g., studying computational physics at a high level). This is almost certainly *not* the best first language for a high school student.\n",
       "\n",
       "---\n",
       "\n",
       "### My Recommendation:\n",
       "\n",
       "**Start with Python.**\n",
       "\n",
       "**Why:** It offers the smoothest entry into the world of programming, provides broad versatility for various interests (data, web, games, automation), has an immense support network, and allows you to build cool projects relatively quickly. It's an excellent foundation that will make learning other languages (like JavaScript, if you later decide to dive into web development) much easier.\n",
       "\n",
       "**After Python (or if you have a strong web interest):**\n",
       "If you find you love programming and want to explore further, **JavaScript** would be an excellent second language, especially if you're drawn to creating things on the web. Python and JavaScript complement each other very well.\n",
       "\n",
       "Good luck on your programming journey! It's a fantastic skill to learn."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"\"\"I'm a high school student. Which of these activities do you suggest and why:\n",
    "a) learn Python\n",
    "b) learn JavaScript\n",
    "c) learn Fortran\n",
    "\"\"\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "iTd60b1GdIsx"
   },
   "source": [
    "### Improve response quality by including examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "yJi44NejdJYE"
   },
   "source": [
    "Another way to improve response quality is to add examples in your prompt. The LLM learns in-context from the examples on how to respond. Typically, one to five examples (shots) are enough to improve the quality of responses. Including too many examples can cause the model to over-fit the data and reduce the quality of responses.\n",
    "\n",
    "Similar to classical model training, the quality and distribution of the examples is very important. Pick examples that are representative of the scenarios that you need the model to learn, and keep the distribution of the examples (e.g. number of examples per class in the case of classification) aligned with your actual distribution."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "sMbLginWdOKs"
   },
   "source": [
    "#### Zero-shot prompt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Crh2Loi2dQ0v"
   },
   "source": [
    "Below is an example of zero-shot prompting, where you don't provide any examples to the LLM within the prompt itself."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "id": "-7myRc-SdTQ4"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "Positive"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"\"\"Decide whether a Tweet's sentiment is positive, neutral, or negative.\n",
    "\n",
    "Tweet: I loved the new YouTube video you made!\n",
    "Sentiment:\n",
    "\"\"\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "ucRtPn9SdL64"
   },
   "source": [
    "#### One-shot prompt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "rs0gQH2vdYBi"
   },
   "source": [
    "Below is an example of one-shot prompting, where you provide one example to the LLM within the prompt to give some guidance on what type of response you want."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "id": "iEq-KxGYdaT5"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "negative"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"\"\"Decide whether a Tweet's sentiment is positive, neutral, or negative.\n",
    "\n",
    "Tweet: I loved the new YouTube video you made!\n",
    "Sentiment: positive\n",
    "\n",
    "Tweet: That was awful. Super boring 😠\n",
    "Sentiment:\n",
    "\"\"\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JnKLjJzmdfL_"
   },
   "source": [
    "#### Few-shot prompt"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "6Zv-9F5OdgI_"
   },
   "source": [
    "Below is an example of few-shot prompting, where you provide a few examples to the LLM within the prompt to give some guidance on what type of response you want."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "id": "u37P9tG4dk9S"
   },
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "positive"
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = \"\"\"Decide whether a Tweet's sentiment is positive, neutral, or negative.\n",
    "\n",
    "Tweet: I loved the new YouTube video you made!\n",
    "Sentiment: positive\n",
    "\n",
    "Tweet: That was awful. Super boring 😠\n",
    "Sentiment: negative\n",
    "\n",
    "Tweet: Something surprised me about this video - it was actually original. It was not the same old recycled stuff that I always see. Watch it - you will not regret it.\n",
    "Sentiment:\n",
    "\"\"\"\n",
    "\n",
    "response = client.models.generate_content(model=MODEL_ID, contents=prompt)\n",
    "display(Markdown(response.text))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "wDMD3xb2dvX6"
   },
   "source": [
    "#### Choosing between zero-shot, one-shot, few-shot prompting methods"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "s92W0YpNdxJp"
   },
   "source": [
    "Which prompt technique to use will solely depends on your goal. The zero-shot prompts are more open-ended and can give you creative answers, while one-shot and few-shot prompts teach the model how to behave so you can get more predictable answers that are consistent with the examples provided."
   ]
  }
 ],
 "metadata": {
  "colab": {
   "name": "intro_prompt_design.ipynb",
   "toc_visible": true
  },
  "environment": {
   "kernel": "conda-base-py",
   "name": "workbench-notebooks.m137",
   "type": "gcloud",
   "uri": "us-docker.pkg.dev/deeplearning-platform-release/gcr.io/workbench-notebooks:m137"
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel) (Local)",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.19"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
