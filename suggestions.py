def get_suggestions(face_shape, skin_tone):
    suggestions = {}

    # Makeup suggestion example
    makeup_suggestions = {
        "Oval": "Try contouring your cheekbones to enhance your natural shape.",
        "Round": "Use bronzer to add definition along the jawline.",
        "Square": "Soften your jawline with blush on the apples of your cheeks.",
        "Heart": "Highlight your forehead and chin with light foundation."
    }

    # Hairstyle suggestion example
    hairstyle_suggestions = {
        "Oval": "You can pull off almost any hairstyle, try waves or curls.",
        "Round": "Go for long layers to elongate your face.",
        "Square": "Soft, wispy bangs will balance your jawline.",
        "Heart": "Side-parted hairstyles work best to soften your forehead."
    }

    # Skincare suggestion example by skin tone
    skincare_suggestions = {
        "Light": "Use SPF daily and light moisturizers to keep skin hydrated.",
        "Medium": "Try antioxidants and vitamin C serums for glowing skin.",
        "Dark": "Focus on moisturizing and products with niacinamide for even tone."
    }

    suggestions['makeup'] = makeup_suggestions.get(face_shape, "No suggestion")
    suggestions['hairstyle'] = hairstyle_suggestions.get(face_shape, "No suggestion")
    suggestions['skincare'] = skincare_suggestions.get(skin_tone, "No suggestion")

    return suggestions
