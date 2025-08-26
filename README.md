# EZ-Unwrap for Blender

EZ Unwrap is a Blender add-on that simplifies UV unwrapping for Second Life and other workflows.  
It combines multiple unwrap tools into one action, and highlights unwrapped meshes with a cyan material.

## 🖥️ Compatibility
- Compiled for Blender 3.0. Tested with versions up to Blender 4.5.
- No guaranteed support for versions of Blender pre-3,0,0

## ✨ Features
- Runs **Follow Active Quads** (if possible, otherwise skips)
- Falls back to **Lightmap Pack** if needed
- Runs **Pack Islands**
- Clears old materials and assigns a **new random-named material**
- Material is automatically colored **cyan** for easy visual confirmation

## 📥 Installation
1. Download **EZ-Unwrap.py** from this repository.
2. If you cannot download it directly, copy the text of the code into a notepad page, and save it as EZ-Unwrap.py 
3. Open Blender.  
4. Go to **Edit > Preferences > Add-ons**.  
5. Click **Install...** in the top-right.  
6. Select the `EZ-Unwrap.py` file.  
7. Enable the checkbox next to **EZ-Unwrap** in the add-ons list.

## 🛠 Usage
1. Select your mesh and switch to **Edit Mode**.  
2. Select the faces you want to unwrap.  
3. Open the **UV menu > Unwrap > EZ Unwrap**.  
4. Your selection will be unwrapped and assigned a cyan-highlighted material.

## 📜 License
This project is licensed under the **AGPL-3.0** License – see the [LICENSE](LICENSE) file for details.

---

## 💖 Support

If you’d like to support development, you can leave **[Voluntary Tips](https://www.paypal.me/JoeLucasWearsPants)** via PayPal.  
Thank you for helping keep this project alive!

