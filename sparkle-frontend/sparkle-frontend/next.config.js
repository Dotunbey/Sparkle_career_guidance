
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Fix for Recharts in Next.js 14+ specific environments
  transpilePackages: ['recharts'],
};

module.exports = nextConfig;
