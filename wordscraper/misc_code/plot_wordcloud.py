import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load scientific words data
with open('../data/scientific_words.json', 'r', encoding='utf-8') as f:
    word_counts = json.load(f)

# Customize the word cloud appearance
wordcloud = WordCloud(
    width=1000,
    height=600,
    background_color='white',  # Changing background to white for a different look
    max_words=200,
    colormap='Dark2',  # Using a different colormap for visual appeal
    contour_width=1,
    contour_color='steelblue',
    scale=3
).generate_from_frequencies(word_counts)

# Plot the WordCloud image with a title
plt.figure(figsize=(15, 10))  # Adjust figure size for better display
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)  # Adjust layout to make room for the title if necessary

# Save the figure BEFORE plt.show()
plt.savefig('../assets/website_wordcloud.png', format='png')  # This will overwrite existing file

# Now display the plot
plt.show()