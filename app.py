<!DOCTYPE html>
<html lang="zh-TW">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>基本電學解題高手</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
              sans: ['"Noto Sans TC"', 'sans-serif'],
              handwritten: ['"Ma Shan Zheng"', 'cursive'],
            },
            colors: {
              paper: '#fdfbf7',
              ink: '#2c3e50',
              accent: '#e74c3c',
              highlight: '#f1c40f',
            }
          },
        },
      }
    </script>
    <!-- MathJax for rendering LaTeX formulas -->
    <script>
      window.MathJax = {
        tex: {
          inlineMath: [['$', '$'], ['\\(', '\\)']],
          displayMath: [] // Disable display math to force inline logic where possible
        },
        svg: {
          fontCache: 'global'
        },
        options: {
           enableMenu: false
        }
      };
    </script>
    <script type="text/javascript" id="MathJax-script" async
      src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
    </script>
    <style>
        body {
            background-color: #f3f4f6;
        }
        /* Custom scrollbar for a notebook feel */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1; 
        }
        ::-webkit-scrollbar-thumb {
            background: #888; 
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #555; 
        }

        /* Force MathJax to be inline to prevent block breaking */
        mjx-container[display="true"], mjx-container {
            display: inline-block !important;
            margin: 0 2px !important;
            vertical-align: middle !important;
            width: auto !important;
        }
        
        /* Ensure paragraph text flows correctly */
        .prose p {
            display: block;
            margin-bottom: 1em;
        }
    </style>
  <script type="importmap">
{
  "imports": {
    "react": "https://esm.sh/react@^19.2.3",
    "react-dom/": "https://esm.sh/react-dom@^19.2.3/",
    "react/": "https://esm.sh/react@^19.2.3/",
    "@google/genai": "https://esm.sh/@google/genai@^1.34.0",
    "react-markdown": "https://esm.sh/react-markdown@9?bundle"
  }
}
</script>
</head>
  <body>
    <div id="root"></div>
  </body>
</html>
