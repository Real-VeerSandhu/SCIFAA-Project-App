mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
[theme]\n\
base=\"light\"\n\
primaryColor=\"#0024ff\"\n\
font=\"serif\"\n\
" > ~/.streamlit/config.toml