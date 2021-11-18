module.exports = {
  pathPrefix: `/LowQualityPoems`,
  siteMetadata: {
    title: `chenyu.I/O`,
  },
  plugins: [
    {
      resolve: `gatsby-philipps-foam-theme`,
      options: {
        rootNote: "/README",
        contentPath: `${__dirname}/..`,
        ignore: [
          "**/_layouts/**",
          "**/.git/**",
          "**/.github/**",
          "**/.vscode/**",
        ],
      },
    },
  ],
};
