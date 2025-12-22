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
    const PAISA_API_BASE_URL = new sst.Secret("PAISA_API_BASE_URL");

    const vpc = new sst.aws.Vpc("PaisaMcpVpc", {
      az: ["ap-south-1a", "ap-south-1b", "ap-south-1c"],
    });

    const cluster = new sst.aws.Cluster("PaisaMcpCluster", { vpc });

    const service = new sst.aws.Service("PaisaMcpService", {
      cluster,
      dev: false,
      serviceRegistry: {
        port: 8000,
      },
      environment: { PAISA_API_BASE_URL: PAISA_API_BASE_URL.value },
    });

    const api = new sst.aws.ApiGatewayV2("PaisaMcpApi", { vpc });

    api.routePrivate("$default", service.nodes.cloudmapService.arn);
  },
});
