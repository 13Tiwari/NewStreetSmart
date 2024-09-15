import { createClient } from "@propelauth/javascript";

const authClient = createClient({
    // The base URL where your authentication pages are hosted. You can find this under the Frontend Integration section for your project.
    authUrl: "https://37728684005.propelauthtest.com/",
    // If true, periodically refresh the access token in the background. This helps ensure you always have a valid token ready to go. Default true.
    enableBackgroundTokenRefresh: true,
});
