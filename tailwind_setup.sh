echo "....................."
echo "....................."
echo "Adding postcss and autoprefixer"
echo "....................."
echo "....................."
yarn add -W tailwindcss@latest postcss@latest autoprefixer@latest

echo "....................."
echo "....................."
echo "Installing Tailwind"
echo "....................."
echo "....................."
npm install -D tailwindcss

echo "....................."
echo "....................."
echo "Running Tailwind init"
echo "....................."
echo "....................."
npx tailwindcss init

echo "....................."
echo "....................."
echo "Watching tailwind css"
echo "....................."
echo "....................."

npx tailwindcss -i ./core/static/css/input.css -o ./core/static/css/output.css --watch

