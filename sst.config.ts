/// <reference path="./.sst/platform/config.d.ts" />

export default $config({
  app(input) {
    return {
      name: "paisa-mcp",
      removal: input?.stage === "production" ? "retain" : "remove",
      protect: ["production"].includes(input?.stage),
      home: "aws",
    };
  },
  async run() {
    new sst.aws.Function('PaisaMcp', {
      handler: 'functions/src/main.handler',
      runtime: 'python3.11',
      url: true,
    })
  },
});
