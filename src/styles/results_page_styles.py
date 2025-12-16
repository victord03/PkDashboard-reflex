
# Used for titles (e.g. "Super effective against:")
results_title_style = {
    "font_size": "20px",
    "font_weight": "700",
    "color": "#ffffff"
}

# Used for displayed text in the results boxes (e.g. "Ice, Grass, Bug")
results_text_style = {
    "font_size": "16px",
    "padding_y": "4px",
    "color": "#f7fafc",
    "text_transform": "capitalize",
}

# Stylizing the three result boxes
result_box_style = {
    "width": "600px",
    "padding": "24px",
    "border_radius": "12px",
    "border": "2px solid #e2e8f0",
    "box_shadow": "0 4px 6px rgba(0,0,0,0.1)",
    "background_color": "#414b69",
}

# Stylizing the inner VSTACK component that holds the three effectiveness boxes
results_vstack_style = {
    "spacing": "2",  # Small gap between title and box
    "align_items": "flex-start",  # Left-align the title
    "width": "600px",
}

# Stylizing the outer VSTACK component that holds all other elements in the results page
results_main_vstack_style = {
    "align_items": "center",
    "spacing": "6",  # Spacing between the three sections
    "width": "100%",
    "padding_y": "40px",
}