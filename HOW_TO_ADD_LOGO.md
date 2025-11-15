# How to Add Your Custom Logo

## Method 1: Using Your Logo Image

1. **Copy your logo file** from `C:\Users\rehan\Desktop\Logo\` 
2. **Paste it** to: `blog-management\static\images\logo.png`
3. **Open** `templates/base.html`
4. **Find** the navbar-brand section (around line 60)
5. **Uncomment** these lines:
   ```html
   <img src="{% static 'images/logo.png' %}" alt="BlogHub Logo" style="height: 45px; width: auto; margin-right: 10px;">
   ```
6. **Comment out** or delete the SVG logo section

## Method 2: Keep Current Animated Logo

The current logo has:
- ✅ Animated shine effect
- ✅ Floating animation
- ✅ Gradient colors
- ✅ Hover effects
- ✅ Professional look

No changes needed - it's already enhanced!

## Logo Specifications

If adding custom logo:
- **Format**: PNG with transparent background
- **Size**: 200x200px (will be scaled to 45px height)
- **Colors**: Should match your brand
- **File name**: logo.png

## Current Features

The enhanced logo now has:
1. ✨ Shine animation effect
2. 🎈 Floating animation
3. 🎨 Gradient text "BlogHub"
4. 🔄 Smooth hover rotation
5. 💫 Professional shadows
