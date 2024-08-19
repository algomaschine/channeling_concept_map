import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn3

# Data for Uniqueness Percentage
entities = [
    'Seth (Jane Roberts)', 
    'Michael (Michael Teachings)', 
    'Ra (Law of One)', 
    'Abraham (Esther Hicks)', 
    'Bashar (Darryl Anka)', 
    'The Nine (Phyllis Schlemmer)', 
    'Kryon (Lee Carroll)', 
    'Pleiadians', 
    'Arcturians', 
    'Hathors', 
    'Elohim', 
    'Ashtar Command', 
    'Cassiopeians', 
    'Zeta Reticulans', 
    'Galactic Federation'
]

uniqueness_percentage = [60, 65, 70, 60, 65, 50, 55, 50, 60, 55, 50, 45, 65, 50, 45]

# Plotting the Uniqueness Percentage Bar Chart
plt.figure(figsize=(14, 10))
sns.set(style="whitegrid")
colors = sns.color_palette("Set2", len(entities))

sns.barplot(x=uniqueness_percentage, y=entities, palette=colors)

plt.title('Uniqueness Percentage of Ideas by Channeled Entities', fontsize=18, weight='bold')
plt.xlabel('Uniqueness Percentage (%)', fontsize=14)
plt.ylabel('Channeled Entities', fontsize=14)

# Add percentages on the bars
for index, value in enumerate(uniqueness_percentage):
    plt.text(value + 1, index, f'{value}%', color='black', va="center", fontweight='bold')

plt.tight_layout()
plt.show()

# Detailed Ideas for Venn Diagram Comparison
seth_ideas = {
    "Reality creation through thoughts", "Multidimensional self", "Simultaneous time",
    "Individual reality creation", "Subjective reality"
}
philosophy_ideas = {
    "Free will", "Self-awareness", "Subjective reality", 
    "Interconnectedness", "Existence precedes essence"
}
theology_ideas = {
    "Reincarnation", "Divine guidance", "Interconnectedness", 
    "Spiritual evolution", "Higher beings"
}
ancient_tradition_ideas = {
    "Reincarnation", "Spiritual evolution", "Higher beings", 
    "Guidance from spirits", "Universal consciousness"
}

# Calculate intersections for Venn Diagram (Example: Seth)
venn_data_seth = {
    '100': len(seth_ideas - philosophy_ideas - theology_ideas - ancient_tradition_ideas),
    '010': len(philosophy_ideas - seth_ideas - theology_ideas - ancient_tradition_ideas),
    '001': len(theology_ideas - seth_ideas - philosophy_ideas - ancient_tradition_ideas),
    '110': len(seth_ideas & philosophy_ideas - theology_ideas - ancient_tradition_ideas),
    '101': len(seth_ideas & theology_ideas - philosophy_ideas - ancient_tradition_ideas),
    '011': len(philosophy_ideas & theology_ideas - seth_ideas - ancient_tradition_ideas),
    '111': len(seth_ideas & philosophy_ideas & theology_ideas)
}

# Plotting the Venn Diagram for Seth
plt.figure(figsize=(8, 8))
venn = venn3(subsets=venn_data_seth, set_labels=('Seth (Jane Roberts)', 'Philosophy', 'Theology'))
plt.title('Venn Diagram of Overlapping Ideas (Seth, Philosophy, Theology)', fontsize=16, weight='bold')
plt.show()

# You can create similar Venn diagrams for other entities by defining their specific ideas and overlaps.
