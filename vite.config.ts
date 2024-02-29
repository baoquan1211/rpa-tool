import { defineConfig, loadConfigFromFile } from "vite";
import react from "@vitejs/plugin-react";
import { createHtmlPlugin } from "vite-plugin-html";
import { UserConfig } from "vite";
import path from "path";

interface UserConfigExtend extends UserConfig {
  vite: {
    port: number;
    host: string;
  };
  app: {
    port: number;
    host: string;
    title: string;
  };
}

export default defineConfig(async ({ command, mode }) => {
  const config = (await loadConfigFromFile({ command, mode }, "./config.json"))
    ?.config as UserConfigExtend | undefined;
  if (!config) {
    throw new Error("Could not load config.json");
  }

  return {
    plugins: [
      react(),
      createHtmlPlugin({
        inject: {
          data: config.app,
        },
      }),
    ],

    base: "",
    root: "src",
    publicDir: "../public",
    build: {
      outDir: "../dist",
    },
    server: {
      port: config.vite.port,
    },

    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
  };
});
